import { useEffect, lazy, Suspense } from 'react';
import { useDispatch } from 'react-redux';

import { Routes, Route } from 'react-router-dom';

import Spinner from './components/spinner/spinner.component';
import { checkUserSession } from './store/user/user.action';

const Navigation = lazy(() =>
    import('./routes/navigation/navigation.component')
);

const Home = lazy(() => import('./routes/home/home.component'));
const Authentication = lazy(() => import('./routes/authentication/authentication.component'));
const BuildingsSelect = lazy(() => import('./routes/buildingsSelect/buildings.select.component'));
const HistoricData = lazy(() => import('./routes/historicData/historic.data.component'));
const FlexRequests = lazy(() => import('./routes/flexRequests/flex.requests.component'));
const InsightAnalytics = lazy(() => import('./routes/insightAnalytics/insight.analytics.component'));

const App = () => {
    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(checkUserSession());
    }, []);

    return (
        <Suspense fallback={<Spinner />}>
            <Routes>
                <Route path='/' element={<Navigation />}>
                    <Route index element={<Home />} />
                    <Route path='buildings' element={<BuildingsSelect />} />
                    <Route path='history' element={<HistoricData />} />
                    <Route path='flex' element={<FlexRequests />} />
                    <Route path='insight' element={<InsightAnalytics />} />
                    <Route path='auth' element={<Authentication />} />
                </Route>
            </Routes>
        </Suspense>
    );
};

export default App;
