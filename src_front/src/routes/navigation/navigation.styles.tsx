import styled from 'styled-components';
import { Link } from 'react-router-dom';

export const NavigationContainer = styled.div`
  height: 70px;
  width: 100%;
  display: flex;
  justify-content: space-between;
  margin-bottom: 25px;
`;

export const LogoContainer = styled(Link)`
    height: 100%;
    width: 220px;
    padding: 25px;
    display: flex;
    justify-content: space-between;
`;

export const NavLinks = styled.div`
  width: 50%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: flex-end;
`;

export const NavLink = styled(Link)`
  padding: 10px 15px;
  cursor: pointer;
`;


export const FLEXoptContainer = styled.div`
    display: flex;
    float: right;
    color:#d36c13;
    font-weight:700;
    align-items: center;
    //margin-top:21px;
    //text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;
`;


