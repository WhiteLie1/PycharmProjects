module.exports = class extends think.Controller {
  __before() {

  }
  async addAction() {//向数据库中添加天气信息
    const data = this.post('data')
    console.log(data)
    const weather = await this.mongo('weather').add(data); // 这个find没有功能
    console.log(weather);
  }
  async findAction() { //查找数据库中的温度数据
    const weather_data = this.mongo('weather')
    console.log(weather_data)
    const data = await weather_data.field('weatherlist').select(); // 这个find没有功能
    return this.json(data)
  }
  //查找数据
  //async findAction() {
    //const userId = this.get('user_id');
    //const userList = await this.model('user').where({ user_id: userId }).select();
 // }
 //const advertisement = this.model('advertisement_item');
 ///const data = await advertisement.field('src').select();
 //return this.json(data);//get在params中执行

};
