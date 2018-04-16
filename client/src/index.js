import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router , Route } from "react-router-dom";
import './index.css';
import App from './App';

import registerServiceWorker from './registerServiceWorker';
import { Login } from './components/Login';
import withAuth from './components/withAuth';
import AddPost from './components/AddPost';

ReactDOM.render(
    <Router>
        <div>
        <Route exact path='/' component={withAuth(App)} />
        <Route path='/add_post' component={withAuth(AddPost)}/>
        <Route  path='/login' component={Login} />
        </div>
    </Router>, document.getElementById('root'));
registerServiceWorker();
