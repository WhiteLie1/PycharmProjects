module.exports = class extends think.Controller {
  __before() {

  }
  async addAction() {
    const data = this.post('data')
    const weather = await this.mongo('weather').add(data); // 这个find没有功能
    console.log(weather);
  }

};
