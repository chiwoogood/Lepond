function sample4_execDaumPostcode() {
  var element_layer = document.getElementById('layer'); 
  new daum.Postcode({
      oncomplete: function(data) {

          var roadAddr = data.roadAddress; 
          var extraRoadAddr = ''; 

          if (data.bname !== '' && /[동|로|가]$/g.test(data.bname)) {
              extraRoadAddr += data.bname;
          }
          if (data.buildingName !== '' && data.apartment === 'Y') {
              extraRoadAddr += (extraRoadAddr !== '' ? ', ' + data.buildingName : data.buildingName);
          }
          if (extraRoadAddr !== '') {
              extraRoadAddr = ' (' + extraRoadAddr + ')';
          }

          document.getElementById('postcode').value = data.zonecode; 
          document.getElementById('roadAddress').value = roadAddr;

          // 지번주소가 없으면 숨기기, 있으면 보이게 하기
          var jibunAddressField = document.getElementById('jibunAddress');
          if (data.jibunAddress === '') {
              jibunAddressField.style.display = 'none';
          } else {
              jibunAddressField.style.display = 'block';
              jibunAddressField.value = data.jibunAddress;
          }

          if (roadAddr !== '') {
              document.getElementById('extraAddress').value = extraRoadAddr;
          } else {
              document.getElementById('extraAddress').value = '';
          }

          element_layer.style.display = 'none';
      },
      width: '100%',
      height: '100%'
  }).embed(element_layer);

  element_layer.style.display = 'block';

  document.body.scrollTop = 0; 
  document.documentElement.scrollTop = 0; 
}


const loginForm = document.getElementById('login-form');
const signupForm = document.querySelector('.signup-form');
const loginBtn = document.getElementById('login-btn');
const signupBtn = document.getElementById('signup-btn');

loginBtn.addEventListener('click', () => {
  loginForm.classList.add('active');
  signupForm.classList.remove('active');
  loginBtn.classList.add('active');
  signupBtn.classList.remove('active');
});

signupBtn.addEventListener('click', () => {
  signupForm.classList.add('active');
  loginForm.classList.remove('active');
  signupBtn.classList.add('active');
  loginBtn.classList.remove('active');
});

// Modals
const forgotPasswordLink = document.getElementById('forgot-password-link');
const findIdLink = document.getElementById('find-id-link');
const forgotPasswordModal = document.getElementById('forgot-password-modal');
const findIdModal = document.getElementById('find-id-modal');
const closeModalButtons = document.querySelectorAll('.close-modal');

forgotPasswordLink.addEventListener('click', (event) => {
  event.preventDefault();
  forgotPasswordModal.style.display = 'block';
});

findIdLink.addEventListener('click', (event) => {
  event.preventDefault();
  findIdModal.style.display = 'block';
});

closeModalButtons.forEach(button => {
  button.addEventListener('click', () => {
    forgotPasswordModal.style.display = 'none';
    findIdModal.style.display = 'none';
  });
});

window.addEventListener('click', (event) => {
  if (event.target === forgotPasswordModal) {
    forgotPasswordModal.style.display = 'none';
  }
  if (event.target === findIdModal) {
    findIdModal.style.display = 'none';
  }
});
