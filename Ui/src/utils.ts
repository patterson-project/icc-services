import React, { useEffect, useRef } from "react";

const useDidMountEffect = (
  func: () => void,
  deps: React.DependencyList | undefined
) => {
  const didMount = useRef(false);

  useEffect(() => {
    if (didMount.current) func();
    else didMount.current = true;
    // eslint-disable-next-line
  }, deps);
};

const post = (url: string, body: any) => {
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
  })
    .then(() => {
      return true;
    })
    .catch(() => {
      return false;
    });
};

export { useDidMountEffect, post };
