import React from 'react'
import './App.css'
import Card from './components/Card'
import getIngredients from './api/getIngredients'

function App(props) {

  const ingredients = getIngredients()
  console.log(ingredients)

  return(
    <div>
      <Card {...ingredients}/>
    </div>
  )
}

export default App;
