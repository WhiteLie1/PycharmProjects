// pages/place-order/all-order.js
const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    order_list:[] //订单列表

  },
  click_order:function(e){//点击下单后，跳转到下单信息确认界面
    console.log(e)
    let that = this
    wx.navigateTo({
      url: '/pages/place-order/order-confirmation',
      success: function(res) {
        // 通过eventChannel向被打开页面传送数据.根据每个数组下标来显示每一条特定的数据
        res.eventChannel.emit('acceptDataFromOpenerPage', { data: that.data.order_list[e.currentTarget.dataset.index] })
      }
    })

  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

    //发送请求，获取订单列表
    var that = this
    wx.request({
      url: 'https://whatdoyoudo.club/v1/deliver/order',
      method: 'GET',
      data: {  },
      header: {
        'content-type': 'application/json; charset=utf-8' // 默认值
      },
      success:  (res)=> {
        console.log('订单测试数据',res.data)
        this.setData({
          order_list : res.data
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