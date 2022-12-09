import { Fragment } from 'react';
import { Outlet } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import { selectCurrentUser } from '../../store/user/user.selector';
import { signOutStart } from '../../store/user/user.action';
import { ReactComponent as BeyondLogo } from '../../assets/beyond-logo.svg';

import {
  NavigationContainer,
  NavLinks,
  LogoContainer,
  FLEXoptContainer,
} from './navigation.styles';

/**
 * The Navigation function is a React component that renders a navigation bar and a router outlet.
 * @returns A Fragment with a NavigationContainer, LogoContainer, NavLinks, and Outlet.
 */
const Navigation = () => {
    const dispatch = useDispatch();
    const currentUser = useSelector(selectCurrentUser);
    const signOutUser = () => dispatch(signOutStart());

    return (
        <Fragment>
            <NavigationContainer>
                <LogoContainer to='/'>
                    <BeyondLogo className='logo' />
                    <FLEXoptContainer>FLEXopt</FLEXoptContainer>
                </LogoContainer>
                <NavLinks>

                </NavLinks>
            </NavigationContainer>
            
            <Outlet />
        </Fragment>
        );
    };

/* Exporting the Navigation component. */
export default Navigation;
