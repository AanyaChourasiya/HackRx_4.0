import React from 'react'
import './first.css'
function Second(props) {
  return (
    <div>
        <h2 className='text-center monu my-3 success mx-3' style={{textAlign:"right", fontFamily: "Piazzolla", margin:"none", padding:"none",fontSize:"25px"}} >
            {props.high}
        </h2>
        <h2 className='text-center size-dec success mx-3' style={{textAlign:"right", fontFamily: "Piazzolla", margin:"none", padding:"none",fontSize:"25px"}} >
            {props.high}
        </h2>

    </div>
  )
}

export default Second
