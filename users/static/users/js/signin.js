document.addEventListener("DOMContentLoaded", function () {
  // 로그인 / 회원가입 전환
  const loginForm = document.getElementById('login-form');
  const signupForm = document.querySelector('.signup-form');
  const loginBtn = document.getElementById('login-btn');
  const signupBtn = document.getElementById('signup-btn');
  const loginContainer = document.querySelector('.login-container');

  loginBtn.addEventListener('click', () => {
    loginForm.classList.add('active');
    signupForm.classList.remove('active');
    loginBtn.classList.add('active');
    signupBtn.classList.remove('active');
    loginContainer.classList.remove('signup-mode');
  });

  signupBtn.addEventListener('click', () => {
    signupForm.classList.add('active');
    loginForm.classList.remove('active');
    signupBtn.classList.add('active');
    loginBtn.classList.remove('active');
    loginContainer.classList.add('signup-mode'); // 회원가입 시 넓게
  });

  // 주소 API (다음)
  window.sample4_execDaumPostcode = function () {
    const element_layer = document.getElementById('layer');
    new daum.Postcode({
      oncomplete: function (data) {
        const roadAddr = data.roadAddress;
        let extraRoadAddr = '';

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

        const jibunAddressField = document.getElementById('jibunAddress');
        if (data.jibunAddress === '') {
          jibunAddressField.style.display = 'none';
        } else {
          jibunAddressField.style.display = 'block';
          jibunAddressField.value = data.jibunAddress;
        }

        document.getElementById('extraAddress').value = extraRoadAddr;
        element_layer.style.display = 'none';
      },
      width: '100%',
      height: '100%'
    }).embed(element_layer);

    element_layer.style.display = 'block';
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
  };

  // 모달: 비밀번호 찾기 & 아이디 찾기
  const forgotPasswordLink = document.getElementById('forgot-password-link');
  const findIdLink = document.getElementById('find-id-link');
  const forgotPasswordModal = document.getElementById('forgot-password-modal');
  const findIdModal = document.getElementById('find-id-modal');
  const closeModalButtons = document.querySelectorAll('.close-modal');

  forgotPasswordLink?.addEventListener('click', (e) => {
    e.preventDefault();
    forgotPasswordModal.style.display = 'block';
  });

  findIdLink?.addEventListener('click', (e) => {
    e.preventDefault();
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
});
