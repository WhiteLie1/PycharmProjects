// pages/transtest/transtest.js
const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    expressNu: null, //订单号
    expressInfo: null //订单信息

  },
 //nu为快递单号
 getExpressInfo: function(nu, cb) {
  wx.request({
    url: 'http://ali-deliver.showapi.com/showapi_expInfo?com=auto&nu=' + nu, 
    data: {
      x: '',
      y: ''
    },
    header: {
      'Authorization': '882c19df-ee08-4c2d-9d10-ccdc172345b5'
    },
    success: function(res) {
      //console.log(res.data)
      cb(res.data) //将数据返回
    }
  })
},
 //输入框输入订单号后赋值
 input: function(e) {
  this.setData({
    expressNu: e.detail.value
  })
},
 //点击查询按钮后获取信息并赋值
 btnClick: function() {
  var thispage = this;
  this.getExpressInfo(this.data.expressNu, function(data) {
    console.log(data)
    console.log(data.showapi_res_body.data)
    thispage.setData({
      expressInfo: data.showapi_res_body.data//格式转换*谨记
    })
  });
},
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

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