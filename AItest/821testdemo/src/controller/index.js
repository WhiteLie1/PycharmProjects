const Base = require('./base.js');
// controller就是用来编写业务逻辑的
module.exports = class extends Base {
  indexAction() {
    return this.display();
  }
};
