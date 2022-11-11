import { useSelector } from 'react-redux';
import { Navigate, Outlet } from 'react-router-dom';
import { selectCurrentUser } from '../../store/user/user.selector';


const Home = () => {
    const currentUser = useSelector(selectCurrentUser);

    return (
        <div>
            {currentUser ? <Navigate to="/buildings" /> : <Navigate to="/auth" />}
            <Outlet />
        </div>
    );
};

export default Home;
//{//<Authentication />}