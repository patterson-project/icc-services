import React, { useEffect, useRef } from 'react';

const useDidMountEffect = (func: () => void, deps: React.DependencyList | undefined) => {
    const didMount = useRef(false);

    useEffect(() => {
        if (didMount.current) func();
        else didMount.current = true;
    // eslint-disable-next-line
    }, deps);
}

export default useDidMountEffect;