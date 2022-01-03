<template>
  <div class="page-register">
    <article class="header">
      <header>
        <el-avatar icon="el-icon-user-solid" shape="circle"></el-avatar>
        <span class="login">
          <em class="bold">Already have an account?</em>
          <a href="#/login">
            <el-button type="primary" size="small">login</el-button>
          </a>
        </span>
      </header>
    </article>
    <el-steps :active="active" finish-status="success">
      <el-step title="Step 1"></el-step>
      <el-step title="Step 2"></el-step>
    </el-steps>

    <section>
      <el-form
        ref="ruleForm"
        :model="ruleForm"
        :rules="rules"
        label-width="100px"
        class="demo-ruleForm"
        autocomplete="off"
      >
        <div v-if="active==0">
          <el-form-item prop="textarea">
            <el-input
              :value="ruleForm.textarea"
              type="textarea"
              :rows="10"
              :readonly="true"
            >
            </el-input>
          </el-form-item>
          <el-form-item prop="agreed">
            <el-checkbox v-model="ruleForm.agreed">Agree</el-checkbox>
          </el-form-item>
        </div>
        <div v-if="active==1">
          <el-form-item label="username" prop="name">
            <el-input v-model="ruleForm.name" />
          </el-form-item>
          <el-form-item label="email" prop="email">
            <el-input v-model="ruleForm.email" />
            <el-button size="mini" round @click="sendMsg">send certification</el-button>
            <span class="status">{{ statusMsg }}</span>
          </el-form-item>
          <el-form-item label="vertification" prop="code">
            <el-input v-model="ruleForm.code" maxlength="4" />
          </el-form-item>
          <el-form-item label="password" prop="pwd">
            <el-input v-model="ruleForm.pwd" type="password" />
          </el-form-item>
          <el-form-item label="password certification" prop="cpwd">
            <el-input v-model="ruleForm.cpwd" type="password" />
          </el-form-item>

        </div>
      </el-form>
    </section>
    <div class="footer">
      <el-button
        v-if="active>0"
        type="primary"
        icon="el-icon-arrow-left"
        @click="prev"
      >last step</el-button>
      <el-button
        v-if="active<step-1"
        type="primary"
        icon="el-icon-arrow-right"
        @click="next"
      >next step</el-button>
      <el-button
        v-if="active==step-1"
        type="primary"
        @click="register"
      >agree and register</el-button>
      <div class="error">{{ error }}</div>
    </div>
  </div>
</template>

<script>
import Axios from 'axios'

export default {
  data() {
    return {
      step: 2,
      active: 0,
      statusMsg: '',
      error: '',
      ruleForm: {
        textarea: 'please read the protical',
        agreed: false,
        name: '',
        code: '',
        pwd: '',
        cpwd: '',
        email: ''
      },
      rules: {
        agreed: [{
          validator: (rule, value, callback) => {
            console.log('value:' + value)
            if (value !== true) {
              callback(new Error('please agree'))
            } else {
              callback()
            }
          },
          trigger: 'blur'
        }],
        name: [{
          required: true,
          type: 'string',
          message: 'enter username',
          trigger: 'blur'
        }],
        email: [{
          required: true,
          type: 'email',
          message: 'enter email',
          trigger: 'blur'
        }],
        pwd: [{
          required: true,
          message: 'create password',
          trigger: 'blur'
        }],
        cpwd: [{
          required: true,
          message: 'certify password',
          trigger: 'blur'
        }, {
          validator: (rule, value, callback) => {
            if (value === '') {
              callback(new Error('please enter your password again'))
            } else if (value !== this.ruleForm.pwd) {
              callback(new Error('the two passwords don\'t match'))
            } else {
              callback()
            }
          },
          trigger: 'blur'
        }]
      }
    }
  },
  layout: 'blank',
  methods: {
    sendMsg: function() {
      const self = this
      let namePass
      let emailPass
      if (self.timerid) {
        return false
      }
      this.$refs['ruleForm'].validateField('name', (valid) => {
        namePass = valid
      })
      self.statusMsg = ''
      if (namePass) {
        return false
      }
      this.$refs['ruleForm'].validateField('email', (valid) => {
        emailPass = valid
      })
      // 模拟验证码发送
      if (!namePass && !emailPass) {
        Axios
          .post("http://127.0.0.1:8000/user/sendEmailCode/", {
            params:{
              mail: this.email
            }
          })
        let count = 60
        self.statusMsg = `critification sent,${count--}seconds remain`
        self.timerid = setInterval(function() {
          self.statusMsg = `critification sent,${count--}seconds remain`
          if (count === 0) {
            clearInterval(self.timerid)
          }
        }, 1000)
      }
    },

    next: function() {
      if (this.active === 0) {
        this.$refs['ruleForm'].validateField('agreed', (valid) => {
          if (valid === '') {
            this.active++
          }
        })
      }
    },
    prev: function() {
      if (--this.active < 0) this.active = 0
    },

    // 模拟登录
    register: function() {
      this.$refs['ruleForm'].validate((valid) => {
        if (valid) {
          Axios
            .post("http://127.0.0.1:8000/register/", {
              params:{
                code: this.code,
                username: this.name,
                password: this.pwd,
                mail: this.email
              }
            })
            .catch(function(error){
              console.log(error);
            });
          setTimeout(
            this.$router.push('/login'), 2000
          )
        }
      })
    }
  }
}
</script>

<style  rel="stylesheet/scss" lang="scss">
.page-register {
  .header {
    //border-bottom: 2px solid rgb(235, 232, 232);
    min-width: 980px;
    color: #666;

    header {
      margin: 0 auto;
      padding: 10px 0;
      width: 980px;

    .login {
        float: right;
      }

      .bold {
        font-style: normal;
      }
    }
  }

  .register {
    color: #1890ff;
  }

  a {
    color: #1890ff;
    text-decoration: none;
    background-color: transparent;
    outline: none;
    cursor: pointer;
    transition: color 0.3s;
  }

  > section {
    margin: 0 auto 30px;
    padding-top: 30px;
    width: 980px;
    min-height: 300px;
    padding-right: 550px;
    box-sizing: border-box;

    .status {
      font-size: 12px;
      margin-left: 20px;
      color: #e6a23c;
    }

    .error {
      color: red;
    }
  }

  .footer{
    text-align: center;
  }
}
</style>

