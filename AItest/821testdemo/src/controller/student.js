const Base = require('./base.js');
// controller就是用来编写业务逻辑的
module.exports = class extends Base {
  async addAction() {
    const student = await this.mongo('student').find(); // 这个find没有功能
    console.log(student);
    if(think.isEmpty(student)) {
      return this.fail();
    }else{
      return this.json({'data':student});
    }
  }
};
