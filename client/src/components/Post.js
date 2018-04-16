
import React from 'react'
import './post.css';

const Post = (props) => {
    return (
        <div className="card">
          
            <img src="http://www.abbeyjfitzgerald.com/wp-content/uploads/2017/02/image-example-02.jpg" alt="Norwegian boller"/>
                <div className="card-content">
                    <h2><b>{props.post.title}</b></h2>
                    <p>{props.post.content}</p>
                </div>
        
        </div>
    )
}

export default Post
