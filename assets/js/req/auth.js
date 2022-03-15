
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
var base_url = 'http://127.0.0.1:8000'
Vue.createApp({
  delimiters: ['[[', ']]'],
  data() {
    return {
      first_name:'',
      last_name: '',
      username: '',
      email: '',
      pasword: '',

      current_pass: '',
      new_pass: '',
      sendingmail: false,
      code: '1',
      otp: '',
      view_box: false,

      actype: 0,
      signingup: false,
      loggingin: false,
      checked: false,

      finval: false,
      linval: false,
      uinval: false,
      minval: false,
      pinval: false,
      acinval: false,

      strength: 0,
    }
  },
  methods: {
    // signup & sign in validation
    fnameval() {
      if (_.size(this.first_name) < 3) {
        this.finval = true;
      } else {
        this.finval = false;
      }
    },
    lnameval() {
      if (_.size(this.last_name) < 3) {
        this.linval = true;
      } else {
        this.linval = false;
      }
    },
    unameval() {
      if (_.size(this.username) < 5) {
        this.uinval = true;
      } else {
        this.uinval = false;
      }
    },
    mailval() {
      if(this.emailvalidate(this.email)) {
        this.minval = false;
      } else {
        this.minval = true;
      }
    },
    pval() {
      if (_.size(this.password) < 8) {
        this.pinval = true;
      } else {
        this.pinval = false;
      }
    },
    lgin() {
      if(_.size(this.username) < 5 ) {
        this.err("username must beat least 5 characters.")
        return
      }
      if(_.size(this.password) < 8 ) {
        this.err("Password must beat least 8 characters.")
        return
      }

      this.loggingin = true
      axios.post('/accounts/login/', {
        username: this.username,
        password: this.password,
      })
        .then((response) => {
          if (response.data.status == 200) {
            window.location.href = "/";
          }
          this.loggingin = false
        }, (error) => {
          if (error.response.status == 404) {
            this.err("Invalid username or password entered!")
          }
          this.loggingin = false
        });
    },
    change() {
      if(_.size(this.current_pass) < 1 ) {
        this.err("You must enter current password")
        return
      }
      if(_.size(this.new_pass) < 8 ) {
        this.err("New password must at least 8 characters.")
        return
      }
      this.sendingmail = true
      axios.post('/accounts/change-password/', {
        current_pass: this.current_pass,
        new_pass: this.new_pass,
        code: this.code,
        otp: this.otp,
      })
        .then((response) => {
          if (response.data.status == 200) {
            this.code = response.data.code
            this.sendingmail = false
            this.view_box = true
          }
          if (response.data.status == 201) {
            window.location.href = '/'
          }
        }, (error) => {
          if (error.response.status == 404) {
            this.err("you entered wrong old password")
          }
          if (error.response.status == 405) {
            this.err("Otp did not match! Try Refreshing this page, and request again!")
          }
          this.sendingmail = false
        });
    },
    signup() {
      this.strength = 0
      if(_.size(this.first_name) < 3 || _.size(this.last_name) < 3) {
        this.err("First name & last name must beat least 3 characters.")
        return
      }
      if(_.size(this.username) < 5 ) {
        this.err("username must beat least 5 characters.")
        return
      }
      if(!this.emailvalidate(this.email)) {
        this.err("Invalid email address entered.")
        return
      }
      if(_.size(this.password) < 8 ) {
        
        this.err("Password must beat least 8 characters.")
        return
      }

      if (this.password.match(/[a-z]+/)) {
        this.strength += 1;
      }
      if (this.password.match(/[A-Z]+/)) {
        this.strength += 1;
      }
      if (this.password.match(/[0-9]+/)) {
        this.strength += 1;
      }
      if (this.password.match(/[$@#&!]+/)) {
        this.strength += 1;
      }
      if (this.strength < 4) {
        this.err("Password must have atleast one uppercase letter, lowercase letter, number and special character.")
        return
      }

      if(this.actype == '0' || this.actype == '') {
        this.err("You must select the account type.")
        return
      }
      if (this.checked == false) {
        this.err("You must accept term and conditions.")
        return
      }

      this.signingup = true
      axios.post('/accounts/signup/', {
        first_name: this.first_name,
        last_name: this.last_name,
        username: this.username,
        email: this.email,
        password: this.password,
        actype: this.actype,
      })
        .then((response) => {
          this.signingup = false
          if (response.data.status == 200) {
            this.err("success")
          }
          if (response.data.status == 201) {
            window.location.href = '/accounts/verify/'
          }
        }, (error) => {
          this.signingup = false
          if(error.response.status == 409) {
            this.err("Username " + this.username + " already exists. Please choose a different one!")
          }
        });
    },
    forget() {

    },
    emailvalidate(m) {
      let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
      if (m.match(regexEmail)) {
        return true; 
      } else {
        return false; 
      }
    },
    err(msg) {
      Lobibox.notify('error', {
        pauseDelayOnHover: true,
        
        rounded: true,
        delayIndicator: true,
        icon: 'bx bx-x-circle',
        continueDelayOnInactiveTab: false,
        position: 'bottom left',
        msg: msg
      });
    }
  },
}).mount('#app')