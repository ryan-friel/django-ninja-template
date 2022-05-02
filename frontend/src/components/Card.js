 import React from 'react'
 import './Card.css'

function Card(props) {
    return(
        <div className='card-container'>
            <h1>{props.name}</h1>
            <h1>{props.description}</h1>
        </div>
    )
}

export default Card