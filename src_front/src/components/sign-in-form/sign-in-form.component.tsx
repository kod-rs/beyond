import { useState, FormEvent, ChangeEvent } from 'react';
import { useDispatch } from 'react-redux';

import FormInput from '../form-input/form-input.component';
import Button, { BUTTON_TYPE_CLASSES } from '../button/button.component';

import { SignInContainer, ButtonsContainer,FLEXoptContainer } from './sign-in-form.styles';
import {  
  emailSignInStart,
} from '../../store/user/user.action';

import { ReactComponent as BeyondLogo } from '../../assets/beyond-logo.svg';

const defaultFormFields = {
  email: '',
  password: '',
};

const SignInForm = () => {
  const dispatch = useDispatch();
  const [formFields, setFormFields] = useState(defaultFormFields);
  const { email, password } = formFields;

  const resetFormFields = () => {
    setFormFields(defaultFormFields);
  };

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    try {
      dispatch(emailSignInStart(email, password));
      resetFormFields();
    } catch (error) {
      console.log('user sign in failed', error);
    }
  };

  const handleChange = (event: ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setFormFields({ ...formFields, [name]: value });
  };

  return (
      <SignInContainer>
          <div>
              <BeyondLogo className='logo' />
              <FLEXoptContainer>FLEXopt</FLEXoptContainer>
          </div>
          <span>Sign in with your username and password</span>
            <form onSubmit={handleSubmit}>
                <FormInput
                    label='Username'
                    type='string'
                    required
                    onChange={handleChange}
                    name='email'
                    value={email}
                />
                <FormInput
                    label='Password'
                    type='password'
                    required
                    onChange={handleChange}
                    name='password'
                    value={password}
                />
                <ButtonsContainer>
                    <Button type='submit'>Sign In</Button>
                </ButtonsContainer>
            </form>
    </SignInContainer>
  );
};

export default SignInForm;
