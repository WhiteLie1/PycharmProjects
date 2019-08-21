module.exports = class extends think.Mongo { // export是暴露在外面的接口使用的
    find(){
        return this.model('student').select();//db.student.find()
    }

};
