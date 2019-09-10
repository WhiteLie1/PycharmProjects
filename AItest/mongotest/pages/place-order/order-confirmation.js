// pages/place-order/order-confirmation.js
const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    order: [],//订单
    code: '',//秘钥
    order_detail:'',//订单详情
    order_D:''

  },
   //获取用户信息
   get_code: function () {
    var that = this;
    return new Promise(function (resolve, reject) {
      wx.request({
        url: 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx5bdae2d90c6f7d85&secret=92ff59a42025eb7d4eba7e6327c2965d',
        method: 'POST',
        data: {  },
        header: {
          'content-type': 'application/json; charset=utf-8' // 默认值
        },
        success: function (res) {
          console.log('同步测试代码')
          that.data.code = res.data;
          resolve();
        }
      });
    });
  },
  place_order: function (e) {//发送订单的模拟数据
    console.log("这是确认订单的页面数据",e)
    var that = this
    this.get_code().then((res)=>{
      wx.request({
        method: 'POST',
        url: 'https://api.weixin.qq.com/cgi-bin/express/business/order/add?access_token=ACCESS_TOKEN',
        data: {
          "access_token": that.data.code,
          "add_source": 0, //小程序订单
          "order_id": "01234567890123456789", //订单ID，须保证全局唯一，不超过512字节
          "openid": "wx5bdae2d90c6f7d85",
          "delivery_id": "TEST",
          "biz_id": "test_biz_id", //
          "custom_remark": "易碎物品",
          "sender": {
            "name": "张三",
            "tel": "020-88888888",
            "mobile": "18666666666",
            "company": "公司名",
            "post_code": "123456",
            "country": "中国",
            "province": "广东省",
            "city": "广州市",
            "area": "海珠区",
            "address": "XX路XX号XX大厦XX栋XX"
          },
          "receiver": {
            "name": that.data.order_detail.data.address.name,
            
            "mobile": that.data.order_detail.data.phone,
            
            "country": "中国",
            "province": that.data.order_detail.data.address.province,
            "city": that.data.order_detail.data.address.city,
            "area":that.data.order_detail.data.address.area,
            "address": that.data.order_detail.data.address.preciseLocation,
          },
          "shop": {
            "wxa_path": "/index/index?from=waybill&id=01234567890123456789",
            "img_url": that.data.order_D.data.commodityList[0].thumbnail,
            "goods_name": that.data.order_D.data.commodityList[0].name,
            "goods_count": that.data.order_D.data.commodityList[0].amount
          },
          "cargo": {
            "count": 2,
            "weight": 5.5,
            "space_x": 30.5,
            "space_y": 20,
            "space_z": 20,
            "detail_list": [
              {
                "name": "一千零一夜钻石包",
                "count": 1
              },
              {
                "name": "爱马仕铂金包",
                "count": 1
              }
            ]
          },
          "insured": {
            "use_insured": 1,
            "insured_value": 10000
          },
          "service": {
            "service_type": 0,
            "service_name": "标准快递"
          }
        },
        success: (res) => {
          console.log('订单生成')
          console.log(res.data)
          that.setData({
            order: res.data
          })
        }
      })

    })
   
  },


  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    let that = this
    const eventChannel = this.getOpenerEventChannel()
    eventChannel.on('acceptDataFromOpenerPage', function(data) {
      console.log('onloaddata',data)
      that.setData({
        order_detail:data
      })
    });
    //获取订单的详情
  
     wx.request({
      url: app.globalData.serverPath + `/user/order/detail?id=${that.data.order_detail.data._id}`,
       method: 'POST',
       data: { 
       
         storage:'00ac2e64fe5c4afdd9fa25a341bcfa70337e795332a16a98c1cc7109dcb76c5f266827cc9f40a6ffe72429bf1572a907b487917f364edd8b235a697042e18942'
        },
       header: {
         'content-type': 'application/json; charset=utf-8' // 默认值
       },
       success:  (res)=> {
         console.log('订单详情',res.data)
         this.setData({
           order_D : res.data
           
         })
       }
     });


  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})