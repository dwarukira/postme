import React, { Component } from 'react'
import AuthService from '../auth'
export default class AddPost extends Component {
    state = {
        file:null
    }
   

    fileSelectedHandler = event =>{
        console.log(event.target.files[0]);
        const data = new FormData()
        data.append('upload',event.target.files[0], event.target.files[0].name)
        fetch('http://localhost:5000/api/uploads', {
            method:'POST',
            body:data
        }).then(res=>{
            res.json().then(data=>{
                console.log(data);
                
            }).catch(err=>{
               console.log(err);
                
            })
            
        })
         
    }
    render() {
        return (
        <div>
            <input type="file" onChange={this.fileSelectedHandler}/>
            </div>
        )
    }
}
