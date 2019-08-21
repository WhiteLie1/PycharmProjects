const Base = require('./base.js');
// export就是导出到所有人都能用
module.exports = class extends Base {
  indexAction() {
    return this.json({nihao: 'nihao '});
  }
  getAction() {
    return this.json({hello: 'get'});
  }
  butAction() {
    return this.json({hello: 'but'});
  }
};
