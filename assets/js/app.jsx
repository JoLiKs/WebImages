import React, {createElement, useEffect, useRef} from 'react';
import '../css/app.css';


const App = (props) => {
  const refE = useRef(null);


  useEffect(() => {
    if (refE.current) {
      refE.current.innerHTML = 'Hi'}
  }, [])


  return <div ref={refE}/>;
}

export default App;
