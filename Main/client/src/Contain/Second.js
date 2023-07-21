import React from 'react'
import './first.css'
function Second(props) {
  return (
    <div>
        <h2 className='text-center monu my-3 success mx-3' style={{textAlign:"right", fontFamily: "Piazzolla", margin:"none", padding:"none",fontSize:"25px"}} >
            {props.high}
        </h2>
        <h2 style={{textAlign:"right",fontFamily: "Piazzolla", margin:"none",padding:"none"}} className='size-dec text-center monu Success mx-3' >
            Vol: { props.volume}
            </h2> 

    </div>
  )
}

export default Second
