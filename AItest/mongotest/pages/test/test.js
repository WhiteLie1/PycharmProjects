// 引用百度地图微信小程序JSAPI模块 
var bmap = require('../../libs/bmap-wx.js'); 
var wxMarkerData = []; 
Page({ 
    data: { 
        markers: [], 
        latitude: '', 
        longitude: '', 
        rgcData: {} 
    }, 
    makertap: function(e) { 
        var that = this; 
        var id = e.markerId; 
        that.showSearchInfo(wxMarkerData, id); 
    }, 
    onLoad: function() { 
        var that = this; 
        // 新建百度地图对象 
        var BMap = new bmap.BMapWX({ 
            ak: 'UjkaMtK88sGYAO7SzDn90P4QXdxhuNPW' 
        }); 
        var fail = function(data) { 
            console.log(data) 
        }; 
        var success = function(data) { 
          console.log("这个是具体位置的详情")
            console.log(data)
            wxMarkerData = data.wxMarkerData; 
            that.setData({ 
                markers: wxMarkerData 
            }); 
            that.setData({ 
                latitude: wxMarkerData[0].latitude 
            }); 
            that.setData({ 
                longitude: wxMarkerData[0].longitude 
            }); 
        } 
        // 发起regeocoding检索请求 
        BMap.regeocoding({ 
            fail: fail, 
            success: success, 
            iconPath: '../../images/marker_red.png', 
            iconTapPath: '../../images/marker_red.png' 
        }); 
    }, 
    showSearchInfo: function(data, i) { 
        var that = this; 
        that.setData({ 
            rgcData: { 
                address: '地址：' + data[i].address + '\n', 
                desc: '描述：' + data[i].desc + '\n', 
                business: '商圈：' + data[i].business 
            } 
        }); 
    } 

})