import React, { Component } from 'react';
import './App.css';
import Post from './components/Post';

class App extends Component {
  constructor(props){
    super(props)
    this.state ={
      data:{},
      loading:true
    }

  }

  componentWillMount(){
    console.log(this.props);
    
    const token = localStorage.getItem('id_token')
    fetch('http://localhost:5000/api/posts',{
      headers:{
        Authorization:`JWT ${token}`
      }
    })
    .then((res)=>{
      return res.json()
    }).then((data) =>{
      this.setState({data:data , loading:false})
    }).catch((err)=>{
      console.log(err);
    })
  }

  handleChange(e){
    this.setState({data:e.target.value})
  }

  render() {
    console.log(this.state);

    if(this.state.loading){
      return(
        <p>loading ....</p>
      )
    }
    const posts = this.state.data.posts.map((post)=>(
      <Post post={post}  key={post.id} />
    )) 
    return (
      <div className=''>
      <div className='cards'>
        {posts}
      </div>
      </div>
    );
  }
}

export default App;
