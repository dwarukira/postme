import React, { Component } from 'react'
import AuthService from '../auth';

export class Login extends Component {
    constructor(props){
        super(props)
        this.state ={
            username:'',
            password:''
        }
    
        this.Auth = new AuthService("http://localhost:5000");
    }

    componentWillMount(){
        if(this.Auth.loggedIn()){
            this.props.history.replace('/')
        }
    }
    handleChange(e){
        this.setState({[e.target.name]:e.target.value})
    }

    handleSubmit(e){
        e.preventDefault();

        this.Auth.login(this.state.username, this.state.password)
        .then(res=>{
            this.props.history.replace('/');
            
        })
        .catch(err=>{
            alert(err);
        })
    }
    render() {

        console.log(this.state)
        return (
        <div>
            <form action="" onSubmit={this.handleSubmit.bind(this)}>
                <input type="text" name='username' value={this.state.username} onChange={this.handleChange.bind(this)}/>
                <input type="text" name='password' value={this.state.password} onChange={this.handleChange.bind(this)}/>
                <input type="submit" value="Login"/>
            </form>            
        </div>
        )
    }
}

export default Login
