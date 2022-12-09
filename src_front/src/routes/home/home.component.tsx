import { useSelector } from 'react-redux';
import { Navigate, Outlet } from 'react-router-dom';
import { selectCurrentUser } from '../../store/user/user.selector';


/* Checking if the user is logged in or not. If the user is logged in, it will navigate to the
buildings page. If the user is not logged in, it will navigate to the auth page. */
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
