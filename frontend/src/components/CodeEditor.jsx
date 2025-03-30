import React from 'react';
import { MonacoEditor } from '@monaco-editor/react';

const CodeEditor = ({ code, setCode }) => {
  return (
    <div className="editor-container">
      <MonacoEditor
        height="90vh"
        defaultLanguage="javascript"
        defaultValue={code}
        onChange={(value) => setCode(value)}
        theme="vs-dark"
      />
    </div>
  );
};

export default CodeEditor; 