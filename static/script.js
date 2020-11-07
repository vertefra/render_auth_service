console.log('sanity')

const form = {
  username: '',
  password: '',
}

const usernameInput = document.getElementById('username')
const passwordInput = document.getElementById('password')
const submitButton = document.getElementById('submitBtn')
const warningText = document.getElementsByClassName('warningText')[0]

submitButton.onclick = async ev => {
  ev.preventDefault()
  console.log('click')
  try {
    // fetch on the accountHandler
    const res = await fetch(
      `https://verte-auth-server.herokuapp.com/api/users/${ev.target.name}/accounts/login`,
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: usernameInput.value,
          password: passwordInput.value,
        }),
      }
    )
    const data = await res.json()
    console.log(data)
    if (!data.success) {
      warningText.innerHTML = data.error
    }
    usernameInput.value = ''
    passwordInput.value = ''
  } catch (err) {
    console.log(err)
    usernameInput.value = ''
    passwordInput.value = ''
  }
}
