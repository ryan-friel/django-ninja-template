import axios from 'axios'

const getIngredients = () => {
    let response = axios.get(`http://localhost:8000/api/ingredients`)
    // console.log(response)
    let output = response
    return output
}

export default getIngredients