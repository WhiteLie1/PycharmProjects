const app = getApp()
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
    rgcData: {},
    allresult:{} //二维码上的全部信息
  },
  //逆解析
  makertap: function (e) {
    var that = this;
    var id = e.markerId;
    that.showSearchInfo(wxMarkerData, id);
  },
  onLoad: function (options) {
    var that = this
    //一加载就发送当前天气信息到数据库里面去
   /* wx.request({
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
    })*/
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

  //扫码事件的触发
  scanCode: function (options) {
    console.log("这是扫码的options", options)
    var that = this;
    // 允许从相机和相册扫码
    wx.scanCode({
      success(res) { //这个是一个链式的，一步扣一步的执行下去
        console.log("扫码成功的信息", res)
        that.getPreciseLocation().then((res) => {
          that.setData({ preciseLocation: res.originalData.result })
          console.log("少吗返回的数据", that.data.preciseLocation)
        }).then(() => {
          //获取系统当前的时间 
          var time = util.formatTime(new Date())
          that.setData({
            time: time
          })
          console.log("少吗外面返回的数据", that.data.preciseLocation)
          //console.log(time)
          //console.log(res) //这个是扫码后的所有信息
          // //这里设置一个data数据来接收当前的扫码结果和地理位置信息
          let allresult = {}
          allresult["content"] = res.result //获取二维码的信息
          allresult["timestamp"] = time
          allresult["address"] = that.data.preciseLocation.formatted_address
          allresult["weatherlist"] = that.data.weatherData
          allresult["latitude"]= that.data.latitude
          allresult["longitude"] = that.data.longitude
          console.log('这是二维码所有的信息')
          console.log(allresult)
          that.setData({
            allresult:allresult
          })
        }).then(() => {
          //let allresult = data
          console.log('这个是result',that.data.allresult)
          //发送信息到数据库里面去
          //sendData() {
          wx.request({
            method: 'POST',
            url: 'http://127.0.0.1:8360/weather/add',
            data: {
              data: that.data.allresult
            },
            success: (res) => {
              console.log('这个是发送天气列表')
              console.log(res.data)
              that.setData({
                weatherList: res.data
              })
            }
          })
          // },

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