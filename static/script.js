
const serverEl = document.getElementById("server")
const server = serverEl.dataset.server

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
      `${server}api/users/${ev.target.name}/accounts/login`,
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
    if (!data.success) {
      warningText.innerHTML = data.error
    }
    usernameInput.value = ''
    passwordInput.value = ''

    
    const response = await fetchRedirectUrl(data.redirectURL, data.token)

    console.log(response)
    

  } catch (err) {
    console.log(err)
    usernameInput.value = ''
    passwordInput.value = ''
  }
}


// send the redirect url to the server that will trigger the redirect response
// with authorization token in the header

const fetchRedirectUrl = async (redirectURL, token) => {
  try {  
  const res = await fetch(redirectURL, {
    method: "GET",
    headers: {
      "Set-Cookie": JSON.stringify({"token":token})
    },
    redirect:"follow"
    
  })

  return res

  } catch(err) {
    return err
  }
}