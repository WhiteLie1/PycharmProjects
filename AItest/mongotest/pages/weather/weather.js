// 引用百度地图微信小程序JSAPI模块 
var bmap = require('../../libs/bmap-wx.js');
//获取系统时间
var util = require('../../utils/util.js')
Page({
  data: {
    weatherData: {},
    preciseLocation: {},
    weatherList: [],
    //地理逆解析
    markers: [],
    latitude: '',
    longitude: '',
    rgcData: {}
  },
  //逆解析
  makertap: function (e) {
    var that = this;
    var id = e.markerId;
    that.showSearchInfo(wxMarkerData, id);
  },
  onLoad: function (options) {
    //获取授权
    this.getLocation();
    var that = this;
    this.getWeatherInfo().then((res) => {
      that.setData({ weatherData: res.currentWeather[0] })
      console.log(that.data.weatherData)
    })
  },
  //页面加载时定位到用户实际中心位置
  getLocation: function () {
    var that = this;
    wx.getLocation({
      type: 'wgs84',
      success: function (res) {
        that.setData({
          latitude: res.latitude,
          longitude: res.longitude
        })
      }
    });
  },
  //发送信息到数据库里面去
  sendData() {
    wx.request({
      method: 'POST',
      url: 'http://127.0.0.1:8360/weather/add',
      data: {
        data: that.data.weatherData
      },
      success: (res) => {
        console.log('这个是发送天气列表')
        console.log(res.data)
        that.setData({
          weatherList: res.data
        })
      }
    })

  },
  //扫码事件的触发
  scanCode: function () {
    var that = this;
    // 允许从相机和相册扫码
    wx.scanCode({
      success(res) {
        that.getPreciseLocation().then((res) => {
          that.setData({preciseLocation: res.originalData.result})
          console.log(that.data.preciseLocation)
        })
        // var success = function (data) {
        //   console.log("这个是扫码后的位置的详情")
        //   console.log(data)
        //   wxMarkerData = data.wxMarkerData;
        //   that.setData({
        //     markers: wxMarkerData
        //   });
        //   that.setData({
        //     latitude: wxMarkerData[0].latitude
        //   });
        //   that.setData({
        //     longitude: wxMarkerData[0].longitude
        //   });
        //   var address = that.data.result.addressComponent.formatted_address

        // }

        // console.log(that.address)
        // // 发起regeocoding检索请求 

        // //获取当前时间 
        // var time = util.formatTime(new Date())
        // that.setData({
        //   time: time
        // })
        // //console.log(time)
        // console.log(res)
        // //这里设置一个data数据来接收当前的扫码结果和地理位置信息
        let data = {}
        data["content"] = res.result
        data["timestamp"] = time
        data["address"] = address
        console.log(data)
      }
    })

  },
  getWeatherInfo() {
    let BMap = new bmap.BMapWX({
      ak: 'UjkaMtK88sGYAO7SzDn90P4QXdxhuNPW'
    });
    let promise = new Promise(function (resolve, reject) {
      BMap.weather({
        fail: () => reject('get weather info failed'),
        success: (res) => resolve(res)
      });
    })
    return promise
  },
  getPreciseLocation() {
    let BMap = new bmap.BMapWX({
      ak: 'UjkaMtK88sGYAO7SzDn90P4QXdxhuNPW'
    })
    let promise = new Promise(function (resolve, reject) {
      BMap.regeocoding({
        fail: () => reject('get precise location failed'),
        success: (res) => resolve(res),
        iconPath: '../../images/marker_red.png',
        iconTapPath: '../../images/marker_red.png'
      })
    })
    return promise
  }
})