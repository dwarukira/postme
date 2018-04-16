import React, { Component } from 'react'
import AuthService from "../auth";
import { withRouter } from 'react-router-dom';

export default function withAuth(AuthComponent){
    const Auth  = new AuthService('http://localhost:5000')
    console.log(Auth.getToken());
    
    return class AuthWrapped extends Component{
        constructor(props){
            super(props)
            this.state={
                user:null
            }
        }

        componentWillMount(){
            if(!Auth.loggedIn()){
                console.log(this.props);
                
                this.props.history.replace('/login')
            }
            try{
                Auth.getProfile().then(res=>{
                    this.setState({user:res})
                }).catch(err=>{
                    console.log(err);
                    
                })

            }
            catch(err){
                
                Auth.logout();
                this.props.history.replace('/login')
            }
        }

        render(){
            if(this.state.user){
              return <AuthComponent user={this.state.user} />
            }
            return(null)
        }
    }
}