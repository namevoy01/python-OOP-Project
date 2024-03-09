import React, { useState } from 'react';

const Wizard = () => {
  const [currentStep, setCurrentStep] = useState(1);

  const handleNext = () => {
    setCurrentStep(currentStep + 1);
  };

  const handlePrev = () => {
    setCurrentStep(currentStep - 1);
  };

  return (
    <div>
      <h1>Wizard - Step {currentStep}</h1>

      {currentStep === 1 && (
        <Step1 nextStep={handleNext} />
      )}

      {currentStep === 2 && (
        <Step2 nextStep={handleNext} prevStep={handlePrev} />
      )}

      {currentStep === 3 && (
        <Step3 prevStep={handlePrev} />
      )}
    </div>
  );
};

const Step1 = ({ nextStep }) => {
  return (
    <div>
      <h2>Step 1</h2>
      {/* Add Step 1 content and form elements */}
      <button onClick={nextStep}>Next</button>
    </div>
  );
};

const Step2 = ({ nextStep, prevStep }) => {
  return (
    <div>
      <h2>Step 2</h2>
      {/* Add Step 2 content and form elements */}
      <button onClick={prevStep}>Previous</button>
      <button onClick={nextStep}>Next</button>
    </div>
  );
};

const Step3 = ({ prevStep }) => {
  return (
    <div>
      <h2>Step 3</h2>
      {/* Add Step 3 content and form elements */}
      <button onClick={prevStep}>Previous</button>
    </div>
  );
};

export default Wizard;