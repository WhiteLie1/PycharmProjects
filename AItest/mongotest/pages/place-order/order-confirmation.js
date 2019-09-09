// pages/place-order/order-confirmation.js
const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    order: [],//订单
    code: '',//秘钥
    order_detail:''//订单详情

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
            "name": that.data.address.name,
            "tel": "020-77777777",
            "mobile": "18610000000",
            "company": "公司名",
            "post_code": "654321",
            "country": "中国",
            "province": "广东省",
            "city": "广州市",
            "area": "天河区",
            "address": "XX路XX号XX大厦XX栋XX"
          },
          "shop": {
            "wxa_path": "/index/index?from=waybill&id=01234567890123456789",
            "img_url": "https://mmbiz.qpic.cn/mmbiz_png/OiaFLUqewuIDNQnTiaCInIG8ibdosYHhQHPbXJUrqYSNIcBL60vo4LIjlcoNG1QPkeH5GWWEB41Ny895CokeAah8A/640",
            "goods_name": "一千零一夜钻石包&爱马仕铂金包",
            "goods_count": 2
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
    console.log("这是啥",options.query)
    const eventChannel = this.getOpenerEventChannel()
    eventChannel.on('acceptDataFromOpenerPage', function(data) {
      console.log('onloaddata',data)
      that.setData({
        order_detail:that.res.data
      })
    })

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