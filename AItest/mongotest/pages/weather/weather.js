// 引用百度地图微信小程序JSAPI模块 
var bmap = require('../../libs/bmap-wx.js'); 
Page({ 
    data: { 
        weatherData: '' 
    }, 
    onLoad: function(options) { 
      //获取授权
        this.getLocation();
        var that = this; 
        // 新建百度地图对象 
        var BMap = new bmap.BMapWX({ 
            ak: 'UjkaMtK88sGYAO7SzDn90P4QXdxhuNPW' 
        }); 
        var fail = function(data) { 
            console.log(data) 
        }; 
        var success = function(data) { 
            console.log(data)
            var weatherData = data.currentWeather[0]; 
            weatherData = '城市：' + weatherData.currentCity + '\n' + 'PM2.5：' + weatherData.pm25 + '\n' +'日期：' + weatherData.date + '\n' + '温度：' + weatherData.temperature + '\n' +'天气：' + weatherData.weatherDesc + '\n' +'风力：' + weatherData.wind + '\n'; 
            console.log(weatherData)
            that.setData({ 
                
                weatherData: weatherData 
            }); 
        } 
        // 发起weather请求 
        BMap.weather({ 
            fail: fail, 
            success: success 
        }); 

        //每次一加载就向服务器端发送当前位置信息和温度信息
        wx.request({
          method:'POST',
          url: 'http://101.132.125.136:27017/test',
          data: {
            storage: wx.getStorageSync('storage')
          },
          success: (res) => {
            that.setData({ orderList: res.data })
          }
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
  } 
})