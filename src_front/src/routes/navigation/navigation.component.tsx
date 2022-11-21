import { Fragment } from 'react';
import { Outlet, Navigate } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import { selectCurrentUser } from '../../store/user/user.selector';
import { signOutStart } from '../../store/user/user.action';
import { ReactComponent as BeyondLogo } from '../../assets/beyond-logo.svg';

import {
  NavigationContainer,
  NavLinks,
  NavLink,
  LogoContainer,
} from './navigation.styles';
import Authentication from '../authentication/authentication.component';
import Home from '../home/home.component';

const Navigation = () => {
    const dispatch = useDispatch();
    const currentUser = useSelector(selectCurrentUser);
    const signOutUser = () => dispatch(signOutStart());

    return (
        <Fragment>
            <NavigationContainer>
                <LogoContainer to='/'>
                    <BeyondLogo className='logo' />
                </LogoContainer>
                <NavLinks>

                </NavLinks>
            </NavigationContainer>
            
            <Outlet />
        </Fragment>
        );
    };

export default Navigation;
