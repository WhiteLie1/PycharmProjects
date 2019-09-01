const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    //图片路径的设置
    tempFilePaths: ''  //如果加了s 则是一个数组
    // scanPhotoPath:'' 拍照图片的地址
  },
  
  /**拍照事件的产生 */
  takePhoto() {
    wx.showToast({ title: '上传中'})
    this.ctx.takePhoto({
      quality: 'high',
      success: (res) => {
        this.setData({
          tempFilePaths: res.tempImagePath //照相的照片存档的地址和相册的地址
          
        })
      }
    })
  },
  error(e) {
    console.log(e.detail)
  },
  //选择照片的时候
  chooseimage: function() {
    var that = this;
    wx.chooseImage({
      sizeType: ['original', 'compressed'],
      sourceType: ['album','camera'],
      success: function(res) {
        console.log(res);
        that.setData({
        tempFilePaths: res.tempFilePaths[0],
        })
      },
      fail:(err) => { console.log(err)}
    })
  },
  startRecord() { //开始上传图片
   // const tempFilePaths = tempFilePaths
   let that = this
    wx.uploadFile({
      //url: 'http://127.0.0.1:8360/user/upload', //这个就是我的后台数据的地址  
      //url: 'http://127.0.0.1:8360/file/upload',
      url: 'http://127.0.0.1:8360/filetest/upload',
      filePath:that.data.tempFilePaths,
      //name: 'file',
      name:'image',
      'method': 'POST',
      header:{    
        'content-type':'application/x-www-form-urlencoded;charset=utf-8'
      },
      success:res => {
        const data = res.data
        console.log(res);
        console.log(this.data.tempFilePaths)
        wx.showToast({
          title: '上传成功',
          //icon: 'loading',
          mask: true,
          duration: 1000,

        })  
      }
      
    })
    
      wx.showToast({
        title: '正在上传',
        icon: 'loading',
        mask: true,
        duration: 1000,
      })

  
},

/**
 * 生命周期函数--监听页面加载
 */
onLoad: function(options) {
  this.ctx = wx.createCameraContext()

},


//图片的选择

//服务器图片的传输



/**
 * 生命周期函数--监听页面初次渲染完成
 */
onReady: function() {},
/**
 * 生命周期函数--监听页面显示
 */
onShow: function() {},
/**
 * 生命周期函数--监听页面隐藏
 */
onHide: function() {
  wx.stopDeviceMotionListening();
},
/** 
 * 生命周期函数--监听页面卸载
 */
onUnload: function() {
  wx.stopDeviceMotionListening();
},
/**
 * 页面相关事件处理函数--监听用户下拉动作
 */
onPullDownRefresh: function() {},
/**
 * 页面上拉触底事件的处理函数
 */
onReachBottom: function() {},
/**
 * 用户点击右上角分享
 */
onShareAppMessage: function() {}
})