import { useEffect, lazy, Suspense } from 'react';
import { useDispatch } from 'react-redux';

import { Routes, Route } from 'react-router-dom';

import Spinner from './components/spinner/spinner.component';
import { checkUserSession } from './store/user/user.action';

const Navigation = lazy(() =>
    import('./routes/navigation/navigation.component')
);

const Home = lazy(() => import('./routes/home/home.component'));
const Authentication = lazy(() =>
    import('./routes/authentication/authentication.component')
);

const App = () => {
    const dispatch = useDispatch();

    useEffect(() => {
        //dispatch(checkUserSession());
    }, []);

    return (
        <Suspense fallback={<Spinner />}>
            <Routes>
                <Route path='/' element={<Navigation />}>
                    <Route index element={<Home />} />
                    <Route path='auth' element={<Authentication />} />
                </Route>
            </Routes>
        </Suspense>
    );
};

export default App;
