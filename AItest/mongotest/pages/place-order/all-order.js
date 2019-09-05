// pages/place-order/all-order.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    order_list:[] //订单列表

  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this
    wx.request({
      url: 'https://whatdoyoudo.club/v1/deliver/order',
      method: 'GET',
      data: {  },
      header: {
        'content-type': 'application/json; charset=utf-8' // 默认值
      },
      success: function (res) {
        console.log('订单测试数据',res.data)
        that.data.order_list = res.data;
        
       
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