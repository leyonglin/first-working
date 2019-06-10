function isCompatible(str){var ua=str||navigator.userAgent;return!!((function(){'use strict';return!this&&Function.prototype.bind&&window.JSON;}())&&'querySelector'in document&&'localStorage'in window&&'addEventListener'in window&&!ua.match(/MSIE 10|webOS\/1\.[0-4]|SymbianOS|Series60|NetFront|Opera Mini|S40OviBrowser|MeeGo|Android.+Glass|^Mozilla\/5\.0 .+ Gecko\/$|googleweblight|PLAYSTATION|PlayStation/));}if(!isCompatible()){document.documentElement.className=document.documentElement.className.replace(/(^|\s)client-js(\s|$)/,'$1client-nojs$2');while(window.NORLQ&&window.NORLQ[0]){window.NORLQ.shift()();}window.NORLQ={push:function(fn){fn();}};window.RLQ={push:function(){}};}else{if(window.performance&&performance.mark){performance.mark('mwStartup');}(function(){'use strict';var mw,StringSet,log,trackQueue=[];function fnv132(str){var hash=0x811C9DC5,i;for(i=0;i<str.length;i++){hash+=(hash<<1)+(hash<<4)+(hash<<7)+(hash<<8)+(hash<<24);hash^=str.charCodeAt(i);}hash=(hash>>>0).toString(36)
;while(hash.length<7){hash='0'+hash;}return hash;}function defineFallbacks(){StringSet=window.Set||function StringSet(){var set=Object.create(null);this.add=function(value){set[value]=!0;};this.has=function(value){return value in set;};};}function setGlobalMapValue(map,key,value){map.values[key]=value;log.deprecate(window,key,value,map===mw.config&&'Use mw.config instead.');}function logError(topic,data){var msg,e=data.exception,source=data.source,module=data.module,console=window.console;if(console&&console.log){msg=(e?'Exception':'Error')+' in '+source;if(module){msg+=' in module '+module;}msg+=(e?':':'.');console.log(msg);if(e&&console.warn){console.warn(e);}}}function Map(global){this.values=Object.create(null);if(global===true){this.set=function(selection,value){var s;if(arguments.length>1){if(typeof selection!=='string'){return false;}setGlobalMapValue(this,selection,value);return true;}if(typeof selection==='object'){for(s in selection){setGlobalMapValue(this,s,selection[s]);}
return true;}return false;};}}Map.prototype={constructor:Map,get:function(selection,fallback){var results,i;fallback=arguments.length>1?fallback:null;if(Array.isArray(selection)){results={};for(i=0;i<selection.length;i++){if(typeof selection[i]==='string'){results[selection[i]]=selection[i]in this.values?this.values[selection[i]]:fallback;}}return results;}if(typeof selection==='string'){return selection in this.values?this.values[selection]:fallback;}if(selection===undefined){results={};for(i in this.values){results[i]=this.values[i];}return results;}return fallback;},set:function(selection,value){var s;if(arguments.length>1){if(typeof selection!=='string'){return false;}this.values[selection]=value;return true;}if(typeof selection==='object'){for(s in selection){this.values[s]=selection[s];}return true;}return false;},exists:function(selection){var i;if(Array.isArray(selection)){for(i=0;i<selection.length;i++){if(typeof selection[i]!=='string'||!(selection[i]in this.values)){return false
;}}return true;}return typeof selection==='string'&&selection in this.values;}};defineFallbacks();log=(function(){var log=function(){},console=window.console;log.warn=console&&console.warn?Function.prototype.bind.call(console.warn,console):function(){};log.error=console&&console.error?Function.prototype.bind.call(console.error,console):function(){};log.deprecate=function(obj,key,val,msg,logName){var stacks;function maybeLog(){var name,trace=new Error().stack;if(!stacks){stacks=new StringSet();}if(!stacks.has(trace)){stacks.add(trace);name=logName||key;mw.track('mw.deprecate',name);mw.log.warn('Use of "'+name+'" is deprecated.'+(msg?(' '+msg):''));}}try{Object.defineProperty(obj,key,{configurable:!0,enumerable:!0,get:function(){maybeLog();return val;},set:function(newVal){maybeLog();val=newVal;}});}catch(err){obj[key]=val;}};return log;}());mw={redefineFallbacksForTest:function(){if(!window.QUnit){throw new Error('Reset not allowed outside unit tests');}defineFallbacks();},now:
function(){var perf=window.performance,navStart=perf&&perf.timing&&perf.timing.navigationStart;mw.now=navStart&&typeof perf.now==='function'?function(){return navStart+perf.now();}:Date.now;return mw.now();},trackQueue:trackQueue,track:function(topic,data){trackQueue.push({topic:topic,timeStamp:mw.now(),data:data});},trackError:function(topic,data){mw.track(topic,data);logError(topic,data);},Map:Map,config:null,libs:{},legacy:{},messages:new Map(),templates:new Map(),log:log,loader:(function(){var registry=Object.create(null),sources=Object.create(null),handlingPendingRequests=!1,pendingRequests=[],queue=[],jobs=[],willPropagate=!1,errorModules=[],baseModules=["jquery","mediawiki.base"],marker=document.querySelector('meta[name="ResourceLoaderDynamicStyles"]'),nextCssBuffer,rAF=window.requestAnimationFrame||setTimeout;function newStyleTag(text,nextNode){var el=document.createElement('style');el.appendChild(document.createTextNode(text));if(nextNode&&nextNode.parentNode){nextNode.
parentNode.insertBefore(el,nextNode);}else{document.head.appendChild(el);}return el;}function flushCssBuffer(cssBuffer){var i;cssBuffer.active=!1;newStyleTag(cssBuffer.cssText,marker);for(i=0;i<cssBuffer.callbacks.length;i++){cssBuffer.callbacks[i]();}}function addEmbeddedCSS(cssText,callback){if(!nextCssBuffer||nextCssBuffer.active===false||cssText.slice(0,'@import'.length)==='@import'){nextCssBuffer={cssText:'',callbacks:[],active:null};}nextCssBuffer.cssText+='\n'+cssText;nextCssBuffer.callbacks.push(callback);if(nextCssBuffer.active===null){nextCssBuffer.active=!0;rAF(flushCssBuffer.bind(null,nextCssBuffer));}}function getCombinedVersion(modules){var hashes=modules.reduce(function(result,module){return result+registry[module].version;},'');return fnv132(hashes);}function allReady(modules){var i;for(i=0;i<modules.length;i++){if(mw.loader.getState(modules[i])!=='ready'){return false;}}return true;}function allWithImplicitReady(module){return allReady(registry[module].
dependencies)&&(baseModules.indexOf(module)!==-1||allReady(baseModules));}function anyFailed(modules){var i,state;for(i=0;i<modules.length;i++){state=mw.loader.getState(modules[i]);if(state==='error'||state==='missing'){return true;}}return false;}function doPropagation(){var errorModule,baseModuleError,module,i,failed,job,didPropagate=!0;do{didPropagate=!1;while(errorModules.length){errorModule=errorModules.shift();baseModuleError=baseModules.indexOf(errorModule)!==-1;for(module in registry){if(registry[module].state!=='error'&&registry[module].state!=='missing'){if(baseModuleError&&baseModules.indexOf(module)===-1){registry[module].state='error';didPropagate=!0;}else if(registry[module].dependencies.indexOf(errorModule)!==-1){registry[module].state='error';errorModules.push(module);didPropagate=!0;}}}}for(module in registry){if(registry[module].state==='loaded'&&allWithImplicitReady(module)){execute(module);didPropagate=!0;}}for(i=0;i<jobs.length;i++){job=jobs[i];failed=
anyFailed(job.dependencies);if(failed||allReady(job.dependencies)){jobs.splice(i,1);i-=1;try{if(failed&&job.error){job.error(new Error('Module has failed dependencies'),job.dependencies);}else if(!failed&&job.ready){job.ready();}}catch(e){mw.trackError('resourceloader.exception',{exception:e,source:'load-callback'});}didPropagate=!0;}}}while(didPropagate);willPropagate=!1;}function requestPropagation(){if(willPropagate){return;}willPropagate=!0;mw.requestIdleCallback(doPropagation,{timeout:1});}function setAndPropagate(module,state){registry[module].state=state;if(state==='loaded'||state==='ready'||state==='error'||state==='missing'){if(state==='ready'){mw.loader.store.add(module);}else if(state==='error'||state==='missing'){errorModules.push(module);}requestPropagation();}}function sortDependencies(module,resolved,unresolved){var i,deps,skip;if(!(module in registry)){throw new Error('Unknown dependency: '+module);}if(registry[module].skip!==null){skip=new Function(registry[
module].skip);registry[module].skip=null;if(skip()){registry[module].skipped=!0;registry[module].dependencies=[];setAndPropagate(module,'ready');return;}}if(resolved.indexOf(module)!==-1){return;}if(!unresolved){unresolved=new StringSet();}if(baseModules.indexOf(module)===-1){baseModules.forEach(function(baseModule){if(resolved.indexOf(baseModule)===-1){resolved.push(baseModule);}});}deps=registry[module].dependencies;unresolved.add(module);for(i=0;i<deps.length;i++){if(resolved.indexOf(deps[i])===-1){if(unresolved.has(deps[i])){throw new Error('Circular reference detected: '+module+' -> '+deps[i]);}sortDependencies(deps[i],resolved,unresolved);}}resolved.push(module);}function resolve(modules){var i,resolved=[];for(i=0;i<modules.length;i++){sortDependencies(modules[i],resolved);}return resolved;}function resolveStubbornly(modules){var i,saved,resolved=[];for(i=0;i<modules.length;i++){saved=resolved.slice();try{sortDependencies(modules[i],resolved);}catch(err){resolved=saved;mw.
trackError('resourceloader.exception',{exception:err,source:'resolve'});}}return resolved;}function addScript(src,callback){var script=document.createElement('script');script.src=src;script.onload=script.onerror=function(){if(script.parentNode){script.parentNode.removeChild(script);}script=null;if(callback){callback();callback=null;}};document.head.appendChild(script);}function queueModuleScript(src,moduleName,callback){pendingRequests.push(function(){if(moduleName!=='jquery'){window.require=mw.loader.require;window.module=registry[moduleName].module;}addScript(src,function(){delete window.module;callback();if(pendingRequests[0]){pendingRequests.shift()();}else{handlingPendingRequests=!1;}});});if(!handlingPendingRequests&&pendingRequests[0]){handlingPendingRequests=!0;pendingRequests.shift()();}}function addLink(media,url){var el=document.createElement('link');el.rel='stylesheet';if(media&&media!=='all'){el.media=media;}el.href=url;if(marker&&marker.parentNode){marker.parentNode.
insertBefore(el,marker);}else{document.head.appendChild(el);}}function domEval(code){var script=document.createElement('script');if(mw.config.get('wgCSPNonce')!==false){script.nonce=mw.config.get('wgCSPNonce');}script.text=code;document.head.appendChild(script);script.parentNode.removeChild(script);}function enqueue(dependencies,ready,error){if(allReady(dependencies)){if(ready!==undefined){ready();}return;}if(anyFailed(dependencies)){if(error!==undefined){error(new Error('One or more dependencies failed to load'),dependencies);}return;}if(ready!==undefined||error!==undefined){jobs.push({dependencies:dependencies.filter(function(module){var state=registry[module].state;return state==='registered'||state==='loaded'||state==='loading'||state==='executing';}),ready:ready,error:error});}dependencies.forEach(function(module){if(registry[module].state==='registered'&&queue.indexOf(module)===-1){if(registry[module].group==='private'){setAndPropagate(module,'error');return;}queue.push(module);}
});mw.loader.work();}function execute(module){var key,value,media,i,urls,cssHandle,siteDeps,siteDepErr,runScript,cssPending=0;if(registry[module].state!=='loaded'){throw new Error('Module in state "'+registry[module].state+'" may not be executed: '+module);}registry[module].state='executing';runScript=function(){var script,markModuleReady,nestedAddScript;script=registry[module].script;markModuleReady=function(){setAndPropagate(module,'ready');};nestedAddScript=function(arr,callback,i){if(i>=arr.length){callback();return;}queueModuleScript(arr[i],module,function(){nestedAddScript(arr,callback,i+1);});};try{if(Array.isArray(script)){nestedAddScript(script,markModuleReady,0);}else if(typeof script==='function'){if(module==='jquery'){script();}else{script(window.$,window.$,mw.loader.require,registry[module].module);}markModuleReady();}else if(typeof script==='string'){domEval(script);markModuleReady();}else{markModuleReady();}}catch(e){setAndPropagate(module,'error');mw.trackError(
'resourceloader.exception',{exception:e,module:module,source:'module-execute'});}};if(registry[module].messages){mw.messages.set(registry[module].messages);}if(registry[module].templates){mw.templates.set(module,registry[module].templates);}cssHandle=function(){cssPending++;return function(){var runScriptCopy;cssPending--;if(cssPending===0){runScriptCopy=runScript;runScript=undefined;runScriptCopy();}};};if(registry[module].style){for(key in registry[module].style){value=registry[module].style[key];media=undefined;if(key!=='url'&&key!=='css'){if(typeof value==='string'){addEmbeddedCSS(value,cssHandle());}else{media=key;key='bc-url';}}if(Array.isArray(value)){for(i=0;i<value.length;i++){if(key==='bc-url'){addLink(media,value[i]);}else if(key==='css'){addEmbeddedCSS(value[i],cssHandle());}}}else if(typeof value==='object'){for(media in value){urls=value[media];for(i=0;i<urls.length;i++){addLink(media,urls[i]);}}}}}if(module==='user'){try{siteDeps=resolve(['site']);}catch(e){siteDepErr=e;
runScript();}if(siteDepErr===undefined){enqueue(siteDeps,runScript,runScript);}}else if(cssPending===0){runScript();}}function sortQuery(o){var key,sorted={},a=[];for(key in o){a.push(key);}a.sort();for(key=0;key<a.length;key++){sorted[a[key]]=o[a[key]];}return sorted;}function buildModulesString(moduleMap){var p,prefix,str=[],list=[];function restore(suffix){return p+suffix;}for(prefix in moduleMap){p=prefix===''?'':prefix+'.';str.push(p+moduleMap[prefix].join(','));list.push.apply(list,moduleMap[prefix].map(restore));}return{str:str.join('|'),list:list};}function resolveIndexedDependencies(modules){var i,j,deps;function resolveIndex(dep){return typeof dep==='number'?modules[dep][0]:dep;}for(i=0;i<modules.length;i++){deps=modules[i][2];if(deps){for(j=0;j<deps.length;j++){deps[j]=resolveIndex(deps[j]);}}}}function makeQueryString(params){return Object.keys(params).map(function(key){return encodeURIComponent(key)+'='+encodeURIComponent(params[key]);}).join('&');}function batchRequest(
batch){var reqBase,splits,maxQueryLength,b,bSource,bGroup,source,group,i,modules,sourceLoadScript,currReqBase,currReqBaseLength,moduleMap,currReqModules,l,lastDotIndex,prefix,suffix,bytesAdded;function doRequest(){var query=Object.create(currReqBase),packed=buildModulesString(moduleMap);query.modules=packed.str;query.version=getCombinedVersion(packed.list);query=sortQuery(query);addScript(sourceLoadScript+'?'+makeQueryString(query));}if(!batch.length){return;}batch.sort();reqBase={skin:mw.config.get('skin'),lang:mw.config.get('wgUserLanguage'),debug:mw.config.get('debug')};maxQueryLength=mw.config.get('wgResourceLoaderMaxQueryLength',2000);splits=Object.create(null);for(b=0;b<batch.length;b++){bSource=registry[batch[b]].source;bGroup=registry[batch[b]].group;if(!splits[bSource]){splits[bSource]=Object.create(null);}if(!splits[bSource][bGroup]){splits[bSource][bGroup]=[];}splits[bSource][bGroup].push(batch[b]);}for(source in splits){sourceLoadScript=sources[source];for(group in splits[
source]){modules=splits[source][group];currReqBase=Object.create(reqBase);if(group==='user'&&mw.config.get('wgUserName')!==null){currReqBase.user=mw.config.get('wgUserName');}currReqBaseLength=makeQueryString(currReqBase).length+25;l=currReqBaseLength;moduleMap=Object.create(null);currReqModules=[];for(i=0;i<modules.length;i++){lastDotIndex=modules[i].lastIndexOf('.');prefix=modules[i].substr(0,lastDotIndex);suffix=modules[i].slice(lastDotIndex+1);bytesAdded=moduleMap[prefix]?suffix.length+3:modules[i].length+3;if(maxQueryLength>0&&currReqModules.length&&l+bytesAdded>maxQueryLength){doRequest();l=currReqBaseLength;moduleMap=Object.create(null);currReqModules=[];mw.track('resourceloader.splitRequest',{maxQueryLength:maxQueryLength});}if(!moduleMap[prefix]){moduleMap[prefix]=[];}l+=bytesAdded;moduleMap[prefix].push(suffix);currReqModules.push(modules[i]);}if(currReqModules.length){doRequest();}}}}function asyncEval(implementations,cb){if(!implementations.length){return;}mw.
requestIdleCallback(function(){try{domEval(implementations.join(';'));}catch(err){cb(err);}});}function getModuleKey(module){return module in registry?(module+'@'+registry[module].version):null;}function splitModuleKey(key){var index=key.indexOf('@');if(index===-1){return{name:key,version:''};}return{name:key.slice(0,index),version:key.slice(index+1)};}function registerOne(module,version,dependencies,group,source,skip){if(module in registry){throw new Error('module already registered: '+module);}registry[module]={module:{exports:{}},version:String(version||''),dependencies:dependencies||[],group:typeof group==='string'?group:null,source:typeof source==='string'?source:'local',state:'registered',skip:typeof skip==='string'?skip:null};}return{moduleRegistry:registry,addStyleTag:newStyleTag,enqueue:enqueue,resolve:resolve,work:function(){var q,batch,implementations,sourceModules;batch=[];for(q=0;q<queue.length;q++){if(queue[q]in registry&&registry[queue[q]].state==='registered'){if(batch.
indexOf(queue[q])===-1){batch.push(queue[q]);registry[queue[q]].state='loading';}}}queue=[];if(!batch.length){return;}mw.loader.store.init();if(mw.loader.store.enabled){implementations=[];sourceModules=[];batch=batch.filter(function(module){var implementation=mw.loader.store.get(module);if(implementation){implementations.push(implementation);sourceModules.push(module);return false;}return true;});asyncEval(implementations,function(err){var failed;mw.loader.store.stats.failed++;mw.loader.store.clear();mw.trackError('resourceloader.exception',{exception:err,source:'store-eval'});failed=sourceModules.filter(function(module){return registry[module].state==='loading';});batchRequest(failed);});}batchRequest(batch);},addSource:function(ids){var id;for(id in ids){if(id in sources){throw new Error('source already registered: '+id);}sources[id]=ids[id];}},register:function(modules){var i;if(typeof modules==='object'){resolveIndexedDependencies(modules);for(i=0;i<modules.length;i++){registerOne.
apply(null,modules[i]);}}else{registerOne.apply(null,arguments);}},implement:function(module,script,style,messages,templates){var split=splitModuleKey(module),name=split.name,version=split.version;if(!(name in registry)){mw.loader.register(name);}if(registry[name].script!==undefined){throw new Error('module already implemented: '+name);}if(version){registry[name].version=version;}registry[name].script=script||null;registry[name].style=style||null;registry[name].messages=messages||null;registry[name].templates=templates||null;if(registry[name].state!=='error'&&registry[name].state!=='missing'){setAndPropagate(name,'loaded');}},load:function(modules,type){var filtered,l;if(typeof modules==='string'){if(/^(https?:)?\/?\//.test(modules)){if(type==='text/css'){l=document.createElement('link');l.rel='stylesheet';l.href=modules;document.head.appendChild(l);return;}if(type==='text/javascript'||type===undefined){addScript(modules);return;}throw new Error(
'invalid type for external url, must be text/css or text/javascript. not '+type);}modules=[modules];}filtered=modules.filter(function(module){var state=mw.loader.getState(module);return state!=='error'&&state!=='missing';});filtered=resolveStubbornly(filtered);enqueue(filtered,undefined,undefined);},state:function(states){var module,state;for(module in states){state=states[module];if(!(module in registry)){mw.loader.register(module);}setAndPropagate(module,state);}},getVersion:function(module){return module in registry?registry[module].version:null;},getState:function(module){return module in registry?registry[module].state:null;},getModuleNames:function(){return Object.keys(registry);},require:function(moduleName){var state=mw.loader.getState(moduleName);if(state!=='ready'){throw new Error('Module "'+moduleName+'" is not loaded.');}return registry[moduleName].module.exports;},store:{enabled:null,MODULE_SIZE_MAX:100*1000,items:{},queue:[],stats:{hits:0,misses:0,expired:0,failed:0},
toJSON:function(){return{items:mw.loader.store.items,vary:mw.loader.store.getVary()};},getStoreKey:function(){return'MediaWikiModuleStore:'+mw.config.get('wgDBname');},getVary:function(){return mw.config.get('skin')+':'+mw.config.get('wgResourceLoaderStorageVersion')+':'+mw.config.get('wgUserLanguage');},init:function(){var raw,data;if(this.enabled!==null){return;}if(/Firefox/.test(navigator.userAgent)||!mw.config.get('wgResourceLoaderStorageEnabled')){this.clear();this.enabled=!1;return;}if(mw.config.get('debug')){this.enabled=!1;return;}try{raw=localStorage.getItem(this.getStoreKey());this.enabled=!0;data=JSON.parse(raw);if(data&&typeof data.items==='object'&&data.vary===this.getVary()){this.items=data.items;return;}}catch(e){mw.trackError('resourceloader.exception',{exception:e,source:'store-localstorage-init'});}if(raw===undefined){this.enabled=!1;}},get:function(module){var key;if(!this.enabled){return false;}key=getModuleKey(module);if(key in this.items){this.stats.
hits++;return this.items[key];}this.stats.misses++;return false;},add:function(module){if(!this.enabled){return;}this.queue.push(module);this.requestUpdate();},set:function(module){var key,args,src,descriptor=mw.loader.moduleRegistry[module];key=getModuleKey(module);if(key in this.items||!descriptor||descriptor.state!=='ready'||!descriptor.version||descriptor.group==='private'||descriptor.group==='user'||[descriptor.script,descriptor.style,descriptor.messages,descriptor.templates].indexOf(undefined)!==-1){return;}try{args=[JSON.stringify(key),typeof descriptor.script==='function'?String(descriptor.script):JSON.stringify(descriptor.script),JSON.stringify(descriptor.style),JSON.stringify(descriptor.messages),JSON.stringify(descriptor.templates)];}catch(e){mw.trackError('resourceloader.exception',{exception:e,source:'store-localstorage-json'});return;}src='mw.loader.implement('+args.join(',')+');';if(src.length>this.MODULE_SIZE_MAX){return;}this.items[key]=src;},prune:function(){var key,
module;for(key in this.items){module=key.slice(0,key.indexOf('@'));if(getModuleKey(module)!==key){this.stats.expired++;delete this.items[key];}else if(this.items[key].length>this.MODULE_SIZE_MAX){delete this.items[key];}}},clear:function(){this.items={};try{localStorage.removeItem(this.getStoreKey());}catch(e){}},requestUpdate:(function(){var hasPendingWrites=!1;function flushWrites(){var data,key;mw.loader.store.prune();while(mw.loader.store.queue.length){mw.loader.store.set(mw.loader.store.queue.shift());}key=mw.loader.store.getStoreKey();try{localStorage.removeItem(key);data=JSON.stringify(mw.loader.store);localStorage.setItem(key,data);}catch(e){mw.trackError('resourceloader.exception',{exception:e,source:'store-localstorage-update'});}hasPendingWrites=!1;}function onTimeout(){mw.requestIdleCallback(flushWrites);}return function(){if(!hasPendingWrites){hasPendingWrites=!0;setTimeout(onTimeout,2000);}};}())}};}()),user:{options:new Map(),tokens:new Map()},widgets:{}};window.
mw=window.mediaWiki=mw;}());(function(){var maxBusy=50;mw.requestIdleCallbackInternal=function(callback){setTimeout(function(){var start=mw.now();callback({didTimeout:!1,timeRemaining:function(){return Math.max(0,maxBusy-(mw.now()-start));}});},1);};mw.requestIdleCallback=window.requestIdleCallback?window.requestIdleCallback.bind(window):mw.requestIdleCallbackInternal;}());(function(){mw.config=new mw.Map(true);mw.loader.addSource({"local":"/load.php"});mw.loader.register([["site","1iwggir",[1]],["site.styles","0jnio9l",[],"site"],["noscript","0r22l1o",[],"noscript"],["filepage","1yjvhwj"],["user.groups","1wjvpdp",[5]],["user","0k1cuul",[],"user"],["user.styles","08fimpv",[],"user"],["user.defaults","1clt4rb"],["user.options","0r5ungb",[7],"private"],["user.tokens","0tffind",[],"private"],["mediawiki.skinning.elements","1m709v7"],["mediawiki.skinning.content","0hjfsz3"],["mediawiki.skinning.interface","093dclz"],["jquery.makeCollapsible.styles","1uhxogk"],[
"mediawiki.skinning.content.parsoid","0bre9zp"],["mediawiki.skinning.content.externallinks","00d96zh"],["jquery","1hra4ln"],["mediawiki.base","007pynj",[16]],["mediawiki.legacy.wikibits","0h66esm",[16]],["jquery.accessKeyLabel","1ocyuac",[25,128]],["jquery.async","02xtsz9"],["jquery.byteLength","0hscdsl",[129]],["jquery.byteLimit","1wjvpdp",[37]],["jquery.checkboxShiftClick","0ut9fx2"],["jquery.chosen","098f6oo"],["jquery.client","1dcrz6x"],["jquery.color","0sc23ww",[27]],["jquery.colorUtil","1njtoga"],["jquery.confirmable","0jpilys",[174]],["jquery.cookie","14spmf1"],["jquery.form","0bzdfr7"],["jquery.fullscreen","0w5nm2b"],["jquery.getAttrs","1ms7eii"],["jquery.hidpi","0c00aux"],["jquery.highlightText","0gfpxi1",[128]],["jquery.hoverIntent","0t5or5x"],["jquery.i18n","1duxvj0",[173]],["jquery.lengthLimit","0jkf0cj",[129]],["jquery.localize","0hf5esh"],["jquery.makeCollapsible","0dp8dte",[13]],["jquery.mockjax","0wyus66"],["jquery.mw-jump","16t49x3"],["jquery.qunit","07bu0vb"],[
"jquery.spinner","0u912gk"],["jquery.jStorage","16ywa17"],["jquery.suggestions","0d9j7pl",[34]],["jquery.tabIndex","13kikah"],["jquery.tablesorter","1wg2j4m",[128,175]],["jquery.textSelection","1d2h6t1",[25]],["jquery.throttle-debounce","0nmngga"],["jquery.xmldom","14khllx"],["jquery.tipsy","0o1t4hn"],["jquery.ui.core","1catuaw",[53],"jquery.ui"],["jquery.ui.core.styles","1drmznw",[],"jquery.ui"],["jquery.ui.accordion","0f9oeal",[52,72],"jquery.ui"],["jquery.ui.autocomplete","0ony4uo",[61],"jquery.ui"],["jquery.ui.button","1gjw4ox",[52,72],"jquery.ui"],["jquery.ui.datepicker","1yxnu01",[52],"jquery.ui"],["jquery.ui.dialog","1043h61",[56,59,63,65],"jquery.ui"],["jquery.ui.draggable","0b136fx",[52,62],"jquery.ui"],["jquery.ui.droppable","0onaol4",[59],"jquery.ui"],["jquery.ui.menu","1z0yngb",[52,63,72],"jquery.ui"],["jquery.ui.mouse","104mype",[72],"jquery.ui"],["jquery.ui.position","0hoybka",[],"jquery.ui"],["jquery.ui.progressbar","18ptoo9",[52,72],"jquery.ui"],["jquery.ui.resizable",
"0cqv62o",[52,62],"jquery.ui"],["jquery.ui.selectable","1me3bub",[52,62],"jquery.ui"],["jquery.ui.slider","1oltn97",[52,62],"jquery.ui"],["jquery.ui.sortable","173dlwj",[52,62],"jquery.ui"],["jquery.ui.spinner","1mhxfu3",[56],"jquery.ui"],["jquery.ui.tabs","1jcn4n8",[52,72],"jquery.ui"],["jquery.ui.tooltip","0pidj84",[52,63,72],"jquery.ui"],["jquery.ui.widget","0ney6rp",[],"jquery.ui"],["jquery.effects.core","0jsamuo",[],"jquery.ui"],["jquery.effects.blind","1i7toxp",[73],"jquery.ui"],["jquery.effects.bounce","1ubtr03",[73],"jquery.ui"],["jquery.effects.clip","1viitpe",[73],"jquery.ui"],["jquery.effects.drop","1bsqjvq",[73],"jquery.ui"],["jquery.effects.explode","0ub8o2j",[73],"jquery.ui"],["jquery.effects.fade","09nyqyf",[73],"jquery.ui"],["jquery.effects.fold","0lhd93n",[73],"jquery.ui"],["jquery.effects.highlight","0aj7xa3",[73],"jquery.ui"],["jquery.effects.pulsate","03mkxrj",[73],"jquery.ui"],["jquery.effects.scale","10hhqqn",[73],"jquery.ui"],["jquery.effects.shake","0iqwowg",[73
],"jquery.ui"],["jquery.effects.slide","15youdr",[73],"jquery.ui"],["jquery.effects.transfer","1fw1egb",[73],"jquery.ui"],["moment","18xhed6",[171]],["mediawiki.apihelp","1m2tpub"],["mediawiki.template","0kl551e"],["mediawiki.template.mustache","0rhhv6x",[89]],["mediawiki.template.regexp","13ycsfk",[89]],["mediawiki.apipretty","1iw1ykx"],["mediawiki.api","0xxaoef",[133,9]],["mediawiki.api.category","1wjvpdp",[93]],["mediawiki.api.edit","1wjvpdp",[93]],["mediawiki.api.login","1wjvpdp",[93]],["mediawiki.api.options","1wjvpdp",[93]],["mediawiki.api.parse","1wjvpdp",[93]],["mediawiki.api.upload","1wjvpdp",[93]],["mediawiki.api.user","1wjvpdp",[93]],["mediawiki.api.watch","1wjvpdp",[93]],["mediawiki.api.messages","1wjvpdp",[93]],["mediawiki.api.rollback","1wjvpdp",[93]],["mediawiki.content.json","1vdakjp"],["mediawiki.confirmCloseWindow","0g89uzf"],["mediawiki.debug","1pcok4m",[262]],["mediawiki.diff.styles","0v64wc9"],["mediawiki.feedback","0ecx16s",[122,267]],["mediawiki.feedlink",
"1vxk4qq"],["mediawiki.filewarning","10q3zs4",[262]],["mediawiki.ForeignApi","0rowaf3",[112]],["mediawiki.ForeignApi.core","0jhdooc",[93,258]],["mediawiki.helplink","1giswmb"],["mediawiki.hlist","1xvezdf"],["mediawiki.htmlform","07arack",[37,128]],["mediawiki.htmlform.checker","1fris6v",[49]],["mediawiki.htmlform.ooui","0ecpzdq",[262]],["mediawiki.htmlform.styles","01mekpv"],["mediawiki.htmlform.ooui.styles","1sxilma"],["mediawiki.icon","17f30gf"],["mediawiki.inspect","1d8a8r9",[128,129]],["mediawiki.messagePoster","00o766p",[111]],["mediawiki.messagePoster.wikitext","1lx8a8r",[122]],["mediawiki.notification","09xfh2y",[146,153]],["mediawiki.notify","0r40aqm"],["mediawiki.notification.convertmessagebox","0tdiz7o",[124]],["mediawiki.notification.convertmessagebox.styles","0jwje6k"],["mediawiki.RegExp","1qrrfxf"],["mediawiki.String","13nkjxu"],["mediawiki.pager.tablePager","1j0f9sz"],["mediawiki.searchSuggest","0ip89em",[32,45,93]],["mediawiki.storage","0kse6bw"],["mediawiki.Title",
"17jog0c",[129,146]],["mediawiki.Upload","0fp5xm7",[93]],["mediawiki.ForeignUpload","0r5wpvm",[111,134]],["mediawiki.ForeignStructuredUpload.config","0msydx9"],["mediawiki.ForeignStructuredUpload","0nvsbvl",[136,135]],["mediawiki.Upload.Dialog","15ywx36",[139]],["mediawiki.Upload.BookletLayout","0rsqvw5",[134,174,144,254,87,264,267]],["mediawiki.ForeignStructuredUpload.BookletLayout","1gq2fhf",[137,139,178,244,238]],["mediawiki.toc","13yppm6",[150]],["mediawiki.toc.styles","17i5hf3"],["mediawiki.Uri","0z62vq9",[146,91]],["mediawiki.user","1v7m8ld",[93,132,8]],["mediawiki.userSuggest","1xneeyn",[45,93]],["mediawiki.util","1m4dysa",[19,125]],["mediawiki.viewport","1976t2t"],["mediawiki.checkboxtoggle","0fj0w4q"],["mediawiki.checkboxtoggle.styles","0ucnypx"],["mediawiki.cookie","1sze54p",[29]],["mediawiki.experiments","12dhb14"],["mediawiki.editfont.styles","1xnr5su"],["mediawiki.visibleTimeout","013sxyf"],["mediawiki.action.delete","1wptit1",[37,262]],["mediawiki.action.delete.file",
"02ma4wc",[37,262]],["mediawiki.action.edit","1mifa8m",[48,157,93,152,240]],["mediawiki.action.edit.styles","1reh7t8"],["mediawiki.action.edit.collapsibleFooter","1v8vnjf",[39,120,132]],["mediawiki.action.edit.preview","14o5r6c",[43,48,93,107,174,262]],["mediawiki.action.history","0z6n8vt"],["mediawiki.action.history.styles","0a5fg6j"],["mediawiki.action.view.dblClickEdit","14x1svg",[146,8]],["mediawiki.action.view.metadata","0fc9v2n",[170]],["mediawiki.action.view.categoryPage.styles","1wnjmdo"],["mediawiki.action.view.postEdit","1s0agl7",[174,124]],["mediawiki.action.view.redirect","1d9abe7",[25]],["mediawiki.action.view.redirectPage","079ebab"],["mediawiki.action.view.rightClickEdit","0f7s7mm"],["mediawiki.action.edit.editWarning","1qo8jdd",[48,105,174]],["mediawiki.action.view.filepage","0daxqnh"],["mediawiki.language","1oveew6",[172]],["mediawiki.cldr","139zmuo",[173]],["mediawiki.libs.pluralruleparser","09cgzow"],["mediawiki.jqueryMsg","1r6u3c3",[171,146,8]],[
"mediawiki.language.months","0ndoh7q",[171]],["mediawiki.language.names","0t6wibh",[171]],["mediawiki.language.specialCharacters","0meovla",[171]],["mediawiki.libs.jpegmeta","02x7zoy"],["mediawiki.page.gallery","14onr7n",[49,180]],["mediawiki.page.gallery.styles","024gyel"],["mediawiki.page.gallery.slideshow","0k518rq",[93,264,281]],["mediawiki.page.ready","13n32zv",[19,23]],["mediawiki.page.startup","0ng567k"],["mediawiki.page.patrol.ajax","1nq20y8",[43,93]],["mediawiki.page.watch.ajax","1equ51t",[93,174]],["mediawiki.page.rollback","1n14q27",[43,93]],["mediawiki.page.image.pagination","0rsym5v",[43,146]],["mediawiki.rcfilters.filters.base.styles","1cp35il"],["mediawiki.rcfilters.highlightCircles.seenunseen.styles","04cqulo"],["mediawiki.rcfilters.filters.dm","1qrdvxv",[143,174,144,258]],["mediawiki.rcfilters.filters.ui","1g06a4f",[39,190,236,275,277,279,281]],["mediawiki.special","1nobj9a"],["mediawiki.special.apisandbox","00s5qs1",[39,93,174,241,261]],["mediawiki.special.block",
"18d7e6j",[115,146,238,245,275]],["mediawiki.special.changecredentials.js","040srbe",[93,117]],["mediawiki.special.changeslist","0udmr2n"],["mediawiki.special.changeslist.enhanced","1o07qmj"],["mediawiki.special.changeslist.legend","0upejeg"],["mediawiki.special.changeslist.legend.js","1t4vuzo",[39,150]],["mediawiki.special.contributions","0t57mr6",[174,238]],["mediawiki.special.edittags","17c6vle",[24,37]],["mediawiki.special.import","1ruwws0"],["mediawiki.special.movePage","10vhh64",[236,240]],["mediawiki.special.pageLanguage","161kwce",[262]],["mediawiki.special.preferences.ooui","14li5hf",[105,152,126,245]],["mediawiki.special.preferences.styles.ooui","0i55prs"],["mediawiki.special.recentchanges","0mwawhu"],["mediawiki.special.revisionDelete","0o0glbw",[37]],["mediawiki.special.search","1p6btu8",[252]],["mediawiki.special.search.commonsInterwikiWidget","15dmpvg",[143,93,174]],["mediawiki.special.search.interwikiwidget.styles","0bxvxpb"],["mediawiki.special.search.styles","0501u7o"]
,["mediawiki.special.undelete","0pioapz",[236,240]],["mediawiki.special.unwatchedPages","0zw6m62",[93]],["mediawiki.special.upload","0il3vdy",[43,93,105,174,178,192,89]],["mediawiki.special.userlogin.common.styles","126dvts"],["mediawiki.special.userlogin.login.styles","06bx5yn"],["mediawiki.special.userlogin.signup.js","1gq7jeq",[93,116,174]],["mediawiki.special.userlogin.signup.styles","116vyhp"],["mediawiki.special.userrights","1g69hf5",[37,126]],["mediawiki.special.watchlist","1wvyr1c",[93,174,262]],["mediawiki.special.version","0yq6e1h"],["mediawiki.legacy.config","0v4b16y"],["mediawiki.legacy.commonPrint","093y953"],["mediawiki.legacy.protect","1fuqojl",[37]],["mediawiki.legacy.shared","100hkut"],["mediawiki.legacy.oldshared","1gv1obt"],["mediawiki.ui","08w3v4o"],["mediawiki.ui.checkbox","1crne50"],["mediawiki.ui.radio","0xwvt23"],["mediawiki.ui.anchor","1wtmfde"],["mediawiki.ui.button","0a9kxrh"],["mediawiki.ui.input","0ny6mkk"],["mediawiki.ui.icon","0ob9wig"],[
"mediawiki.ui.text","0mw1cu3"],["mediawiki.widgets","07btib3",[93,237,264]],["mediawiki.widgets.styles","0mbhn9u"],["mediawiki.widgets.DateInputWidget","0theflm",[239,87,264]],["mediawiki.widgets.DateInputWidget.styles","0i8j8dh"],["mediawiki.widgets.visibleLengthLimit","1dmll1z",[37,262]],["mediawiki.widgets.datetime","1i3bmch",[262,282,283]],["mediawiki.widgets.expiry","08fc1jl",[241,87,264]],["mediawiki.widgets.CheckMatrixWidget","1x9pvek",[262]],["mediawiki.widgets.CategoryMultiselectWidget","0ohaqo2",[111,264]],["mediawiki.widgets.SelectWithInputWidget","08v0e4d",[246,264]],["mediawiki.widgets.SelectWithInputWidget.styles","0dqm8as"],["mediawiki.widgets.SizeFilterWidget","1pzhqff",[248,264]],["mediawiki.widgets.SizeFilterWidget.styles","17ni22j"],["mediawiki.widgets.MediaSearch","1qxijne",[111,264]],["mediawiki.widgets.UserInputWidget","1rxoqik",[93,264]],["mediawiki.widgets.UsersMultiselectWidget","0ovukic",[93,264]],["mediawiki.widgets.SearchInputWidget","1dhjrf2",[131,236]],[
"mediawiki.widgets.SearchInputWidget.styles","1rn8qnq"],["mediawiki.widgets.StashedFileWidget","1uiyvsv",[93,262]],["easy-deflate.core","0g9o4ja"],["easy-deflate.deflate","1rzzfqk",[255]],["easy-deflate.inflate","0juehwn",[255]],["oojs","0mrwini"],["mediawiki.router","1t2pglg",[260]],["oojs-router","1vn0q0a",[258]],["oojs-ui","1wjvpdp",[266,264,267]],["oojs-ui-core","0ilwoob",[171,258,263,271,272,278,268,269]],["oojs-ui-core.styles","1wo4b89"],["oojs-ui-widgets","0wycqha",[262,273,282,283]],["oojs-ui-widgets.styles","1cw83ut"],["oojs-ui-toolbars","0nljh23",[262,283]],["oojs-ui-windows","058ggnb",[262,283]],["oojs-ui.styles.indicators","1opaeiu"],["oojs-ui.styles.textures","07bwp84"],["oojs-ui.styles.icons-accessibility","0aedc29"],["oojs-ui.styles.icons-alerts","1b660e5"],["oojs-ui.styles.icons-content","090dpg7"],["oojs-ui.styles.icons-editing-advanced","1n360wp"],["oojs-ui.styles.icons-editing-citation","0vp80hz"],["oojs-ui.styles.icons-editing-core","1dq3u3x"],[
"oojs-ui.styles.icons-editing-list","1jkiobx"],["oojs-ui.styles.icons-editing-styling","0hwxytm"],["oojs-ui.styles.icons-interactions","057gs4j"],["oojs-ui.styles.icons-layout","1q2viiv"],["oojs-ui.styles.icons-location","0x39zkc"],["oojs-ui.styles.icons-media","11rb2gq"],["oojs-ui.styles.icons-moderation","1blo52s"],["oojs-ui.styles.icons-movement","16a8l9x"],["oojs-ui.styles.icons-user","1mvmr4d"],["oojs-ui.styles.icons-wikimedia","0531awf"],["skins.monobook.styles","1lb3dz6"],["skins.monobook.responsive","1hq1oq5"],["skins.monobook.mobile","0yiozyx",[146]],["skins.vector.styles","10mfj2m"],["skins.vector.styles.responsive","00va31f"],["skins.vector.js","1h48uso",[46,49]],["zzz.ext.archLinux.styles","0fygbnm"],["ext.nuke","0l2q25r"],["ext.nuke.confirm","18vp54b"],["ext.abuseFilter","04t64ag"],["ext.abuseFilter.edit","1ag4ez7",[43,48,93,264]],["ext.abuseFilter.tools","0ztycj1",[43,93]],["ext.abuseFilter.examine","054hrtb",[43,93]],["ext.abuseFilter.ace","0eaw3l1",["ext.codeEditor.ace"
]],["ext.checkUser","0dbo9m7",[146]],["ext.checkUser.caMultiLock","0x1o4h9",[146]],["ext.interwiki.specialpage","02ng7o0"]]);mw.config.set({"wgLoadScript":"/load.php","debug":!1,"skin":"vector","stylepath":"/skins","wgUrlProtocols":"bitcoin\\:|ftp\\:\\/\\/|ftps\\:\\/\\/|geo\\:|git\\:\\/\\/|gopher\\:\\/\\/|http\\:\\/\\/|https\\:\\/\\/|irc\\:\\/\\/|ircs\\:\\/\\/|magnet\\:|mailto\\:|mms\\:\\/\\/|news\\:|nntp\\:\\/\\/|redis\\:\\/\\/|sftp\\:\\/\\/|sip\\:|sips\\:|sms\\:|ssh\\:\\/\\/|svn\\:\\/\\/|tel\\:|telnet\\:\\/\\/|urn\\:|worldwind\\:\\/\\/|xmpp\\:|\\/\\/","wgArticlePath":"/index.php/$1","wgScriptPath":"","wgScript":"/index.php","wgSearchType":null,"wgVariantArticlePath":!1,"wgActionPaths":{},"wgServer":"https://wiki.archlinux.org","wgServerName":"wiki.archlinux.org","wgUserLanguage":"en","wgContentLanguage":"en","wgTranslateNumerals":!0,"wgVersion":"1.32.0","wgEnableAPI":!0,"wgEnableWriteAPI":!0,"wgMainPageTitle":"Main page","wgFormattedNamespaces":{"-2":"Media","-1":
"Special","0":"","1":"Talk","2":"User","3":"User talk","4":"ArchWiki","5":"ArchWiki talk","6":"File","7":"File talk","8":"MediaWiki","9":"MediaWiki talk","10":"Template","11":"Template talk","12":"Help","13":"Help talk","14":"Category","15":"Category talk"},"wgNamespaceIds":{"media":-2,"special":-1,"":0,"talk":1,"user":2,"user_talk":3,"archwiki":4,"archwiki_talk":5,"file":6,"file_talk":7,"mediawiki":8,"mediawiki_talk":9,"template":10,"template_talk":11,"help":12,"help_talk":13,"category":14,"category_talk":15,"image":6,"image_talk":7,"project":4,"project_talk":5},"wgContentNamespaces":[0],"wgSiteName":"ArchWiki","wgDBname":"archwiki","wgExtraSignatureNamespaces":[],"wgAvailableSkins":{"monobook":"MonoBook","vector":"Vector","fallback":"Fallback","apioutput":"ApiOutput"},"wgExtensionAssetsPath":"/extensions","wgCookiePrefix":"archwiki","wgCookieDomain":"","wgCookiePath":"/","wgCookieExpiration":2592000,"wgResourceLoaderMaxQueryLength":-1,"wgCaseSensitiveNamespaces":[],
"wgLegalTitleChars":" %!\"$\u0026'()*,\\-./0-9:;=?@A-Z\\\\\\^_`a-z~+\\u0080-\\uFFFF","wgIllegalFileChars":":/\\\\","wgResourceLoaderStorageVersion":1,"wgResourceLoaderStorageEnabled":!0,"wgForeignUploadTargets":["local"],"wgEnableUploads":!0,"wgCommentByteLimit":255,"wgCommentCodePointLimit":null});var queue=window.RLQ;window.RLQ=[];RLQ.push=function(fn){if(typeof fn==='function'){fn();}else{RLQ[RLQ.length]=fn;}};while(queue&&queue[0]){RLQ.push(queue.shift());}window.NORLQ={push:function(){}};}());}

/* Cached 20190610140720 */