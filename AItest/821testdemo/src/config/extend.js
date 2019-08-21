const view = require('think-view');
const model = require('think-model');
const cache = require('think-cache');
const session = require('think-session');
const mongo = require('think-mongo'); // mongo的配置

module.exports = [
  view, // make application support view
  model(think.app),
  mongo(think.app), // 配置mongo
  cache,
  session
];
