// module.exports = class extends Base {
//   async addAction() {
//     const student = await this.mongo('student').find(); // 这个find没有功能
//     console.log(student);
//     if(think.isEmpty(student)) {
//       return this.fail();
//     }else{
//       return this.json({'data':student});
//     }
//   }
//   //查找数据
//   //async findAction() {
//     //const userId = this.get('user_id');
//     //const userList = await this.model('user').where({ user_id: userId }).select();
//  // }
//   async findAction() { //查找数据库中的温度数据
//     const data = this.get('weather')
//     console.log(data)
//     const weather = await this.mongo('weather').add(data); // 这个find没有功能
//     console.log(weather);
//   }
// };
