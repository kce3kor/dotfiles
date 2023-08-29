exports.id=831,exports.ids=[831],exports.modules={9042:(t,e,i)=>{i.d(e,{TimelineWebviewProvider:()=>TimelineWebviewProvider});var n=i(9496),o=i(5255),s=i(8887),a=i(7462),r=i(6450),h=i(3646),d=i(9529),c=i(5148),l=i(7512),g=i(4241),p=i(9796),u=i(3105),m=i(2509),v=i(6922),C=i(5798),f=i(6260),w=i(1753);const x=new C.jH("timeline/didChange"),b=new C.ke("timeline/point/open"),y=new C.ke("timeline/period/update");var D=Object.defineProperty,S=Object.getOwnPropertyDescriptor,_=(t,e,i,n)=>{for(var o,s=n>1?void 0:n?S(e,i):e,a=t.length-1;a>=0;a--)(o=t[a])&&(s=(n?o(e,i,s):o(s))||s);return n&&s&&D(e,i,s),s};class TimelineWebviewProvider{constructor(t,e){this.container=t,this.host=e,this._context={uri:void 0,period:"3|M",etagRepositories:this.container.git.etag,etagRepository:0,etagSubscription:this.container.subscription.etag},this._context={...this._context,...this._pendingContext},this._pendingContext=void 0,this.host.isEditor()?this._disposable=n.Disposable.from(this.container.subscription.onDidChange(this.onSubscriptionChanged,this),this.container.git.onDidChangeRepository(this.onRepositoryChanged,this)):(this.host.description="✨",this._disposable=n.Disposable.from(this.container.subscription.onDidChange(this.onSubscriptionChanged,this),this.container.git.onDidChangeRepository(this.onRepositoryChanged,this),this.container.git.onDidChangeRepositories(this.onRepositoriesChanged,this),n.window.onDidChangeActiveTextEditor((0,p.Ds)(this.onActiveEditorChanged,250),this),this.container.events.on("file:selected",(0,p.Ds)(this.onFileSelected,250),this)))}_bootstraping=!0;_context;_pendingContext;_disposable;dispose(){this._disposable.dispose()}onReloaded(){this.notifyDidChangeState(!0)}onShowing(t,e,...i){const[o]=i;return null!=o?o instanceof n.Uri?this.updatePendingUri(o):(0,v.w8)(o)?this.updatePendingUri(o.uri):(0,w.W)(o)&&this.updatePendingContext({period:o.state.period,uri:null!=o.state.uri?n.Uri.parse(o.state.uri):void 0}):this.updatePendingEditor(n.window.activeTextEditor),t?(this._context={...this._context,...this._pendingContext},this._pendingContext=void 0):this.updateState(),!0}includeBootstrap(){return this._bootstraping=!0,this._context={...this._context,...this._pendingContext},this._pendingContext=void 0,this.getState(this._context)}registerCommands(){return this.host.isEditor()?[(0,d.xR)(o.Gh.RefreshTimelinePage,(()=>this.host.refresh(!0)))]:[(0,d.xR)(`${this.host.id}.refresh`,(()=>this.host.refresh(!0)),this),(0,d.xR)(`${this.host.id}.openInTab`,(()=>this.openInTab()),this)]}onVisibilityChanged(t){t&&(this.host.isView()&&this.updatePendingEditor(n.window.activeTextEditor),this._bootstraping&&(this._bootstraping=!1,null==this._pendingContext||!("uri"in this._pendingContext))||this.updateState())}onMessageReceived(t){switch(t.method){case b.method:(0,C.mq)(b,t,(async t=>{if(null==t.data||!t.data.selected||null==this._context.uri)return;const e=this.container.git.getRepository(this._context.uri);if(null==e)return;const i=await e.getCommit(t.data.id);null!=i&&(this.container.events.fire("commit:selected",{commit:i,interaction:"active",preserveFocus:!0,preserveVisibility:!1},{source:this.host.id}),this.container.commitDetailsView.ready||this.container.commitDetailsView.show({preserveFocus:!0},{commit:i,interaction:"active",preserveVisibility:!1}))}));break;case y.method:(0,C.mq)(y,t,(t=>{this.updatePendingContext({period:t.period})&&this.updateState(!0)}))}}onActiveEditorChanged(t){if(null!=t){if(!(0,m.PH)(t))return;this.container.git.isTrackable(t.document.uri)||(t=void 0)}this.updatePendingEditor(t)&&this.updateState()}onFileSelected(t){if(null==t.data)return;let e=t.data.uri;null!=e&&(this.container.git.isTrackable(e)||(e=void 0)),this.updatePendingUri(e)&&this.updateState()}onRepositoriesChanged(t){const e=this.updatePendingUri(this._context.uri);(this.updatePendingContext({etagRepositories:t.etag})||e)&&this.updateState()}onRepositoryChanged(t){t.changed(h.I6.Heads,h.I6.Index,h.du.Any)&&this.updatePendingContext({etagRepository:t.repository.etag})&&this.updateState()}onSubscriptionChanged(t){this.updatePendingContext({etagSubscription:t.etag})&&this.updateState()}async getState(t){const e=c.D.get("defaultDateFormat")??"MMMM Do, YYYY h:mma",i=c.D.get("defaultDateShortFormat")??"short",o=t.period??"3|M",h=null!=t.uri?await a.YY.fromUri(t.uri):void 0,d=h?.repoPath;this.host.isEditor()?this.host.title=null==h?this.host.originalTitle:`${this.host.originalTitle}: ${h.fileName}`:this.host.description=h?.fileName??"✨";const l=await this.container.git.access(s.x.Timeline,d);if(null==t.uri||null==h||null==d||!1===l.allowed){const n=await this.container.git.access(s.x.Timeline,d);return{timestamp:Date.now(),period:o,title:h?.relativePath,sha:h?.shortSha,uri:t.uri?.toString(),dateFormat:e,shortDateFormat:i,access:n}}const[g,p]=await Promise.all([this.container.git.getCurrentUser(d),this.container.git.getLogForFile(d,h.fsPath,{limit:0,ref:h.sha,since:P(o)?.toISOString()})]);if(null==p)return{timestamp:Date.now(),dataset:[],period:o,title:h.relativePath,sha:h.shortSha,uri:t.uri.toString(),dateFormat:e,shortDateFormat:i,access:l};let m=[...(0,u.hX)(p.commits.values(),(t=>null==t.file?.stats&&1!==(0,r.By)(t.stats?.changedFiles)))];if(0!==m.length){const e=c.D.get("visualHistory.queryLimit")??20,i=this.container.git.getRepository(t.uri),o=i?.provider.name;m.length>e&&(n.window.showWarningMessage(`Unable able to show more than the first ${e} commits for the specified time period because of ${o?`${o} `:""}rate limits.`),m=m.slice(0,20)),await Promise.allSettled(m.map((t=>t.ensureFullDetails())))}const v=g?.name?`${g.name} (you)`:"You",C=[];for(const t of p.commits.values()){const e=t.file?.stats??(1===(0,r.By)(t.stats?.changedFiles)?t.stats:void 0);C.push({author:"You"===t.author.name?v:t.author.name,additions:e?.additions,deletions:e?.deletions,commit:t.sha,date:t.date.toISOString(),message:t.message??t.summary,sort:t.date.getTime()})}return C.sort(((t,e)=>e.sort-t.sort)),{timestamp:Date.now(),dataset:C,period:o,title:h.relativePath,sha:h.shortSha,uri:t.uri.toString(),dateFormat:e,shortDateFormat:i,access:l}}updatePendingContext(t,e){const[i,n]=(0,f.OY)(this._context,this._pendingContext,t,e);return i&&(this._pendingContext=n),i}updatePendingEditor(t,e){return(null!=t||!(0,m.JM)(this._context.uri??this._pendingContext?.uri))&&(!(null!=t&&!(0,m.PH)(t))&&this.updatePendingUri(t?.document.uri,e))}updatePendingUri(t,e){let i;if(null!=t){const e=this.container.git.getRepository(t);i=e?.etag??0}else i=0;return this.updatePendingContext({uri:t,etagRepository:i},e)}_notifyDidChangeStateDebounced=void 0;updateState(t=!1){t?this.notifyDidChangeState():(null==this._notifyDidChangeStateDebounced&&(this._notifyDidChangeStateDebounced=(0,p.Ds)(this.notifyDidChangeState.bind(this),500)),this._notifyDidChangeStateDebounced())}async notifyDidChangeState(t=!1){if(this._notifyDidChangeStateDebounced?.cancel(),!t&&null==this._pendingContext)return!1;let e;null!=this._pendingContext?(e={...this._context,...this._pendingContext},this._context=e,this._pendingContext=void 0):e=this._context;const i=async()=>this.host.notify(x,{state:await this.getState(e)});return this.host.isView()?n.window.withProgress({location:{viewId:this.host.id}},i):i()}openInTab(){const t=this._context.uri;null!=t&&n.commands.executeCommand(o.Gh.ShowTimelinePage,t)}}function P(t){if("all"==t)return;const[e,i]=t.split("|");let n;switch(i){case"D":n=(0,l.IH)(new Date,{days:-parseInt(e,10)});break;case"M":n=(0,l.IH)(new Date,{months:-parseInt(e,10)});break;case"Y":n=(0,l.IH)(new Date,{years:-parseInt(e,10)});break;default:n=(0,l.IH)(new Date,{months:-3})}return n.getHours()>=12&&n.setDate(n.getDate()+1),n.setHours(0,0,0,0),n}_([(0,g.fF)({args:!1})],TimelineWebviewProvider.prototype,"onActiveEditorChanged",1),_([(0,g.fF)({args:!1})],TimelineWebviewProvider.prototype,"onFileSelected",1),_([(0,g.fF)({args:!1})],TimelineWebviewProvider.prototype,"onRepositoriesChanged",1),_([(0,g.fF)({args:!1})],TimelineWebviewProvider.prototype,"onRepositoryChanged",1),_([(0,g.fF)({args:!1})],TimelineWebviewProvider.prototype,"onSubscriptionChanged",1),_([(0,g.fF)({args:!1})],TimelineWebviewProvider.prototype,"getState",1),_([(0,g.fF)()],TimelineWebviewProvider.prototype,"updateState",1),_([(0,g.fF)()],TimelineWebviewProvider.prototype,"notifyDidChangeState",1)}};