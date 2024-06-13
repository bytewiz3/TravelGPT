(function (global, factory) { 
    typeof exports === 'object' && typeof module !== 'undefined' ? module.exports = factory() : 
    typeof define === 'function' && define.amd ? define(factory) : 
    (global = typeof globalThis !== 'undefined' ? globalThis : global || self, global.readNDJSONStream = factory()); 
})(this, (function () { 'use strict'; 
 
    async function* index (readableStream) { 
        const reader = readableStream.getReader(); 
        let runningText = ""; 
        while (true) { 
            const { done, value } = await reader.read(); 
            if (done) break; 
            var text = new TextDecoder("utf-8").decode(value); 
            const objects = text.split("\n"); 
            for (const obj of objects) { 
                try { 
                    var temp = obj.substring(6); 
                    temp = temp.substring(0, temp.length - 1); 
                    runningText += temp; 
                    let result = JSON.parse(runningText); 
                    yield result; 
                    runningText = ""; 
                } 
                catch (e) { 
                    // Not a valid JSON object 
                } 
            } 
        }} 
 
    return index; 
 
})); 
 
 
