/*
visibility_polygon.js version 1.9

This code is released into the public domain - attribution is appreciated but not required.
Made by Byron Knoll.

https://github.com/byronknoll/visibility-polygon-js
*/

function VisibilityPolygon(){}
VisibilityPolygon.compute=function(d,c){for(var e=[],g=d[0],f=d[1],k=d[0],h=d[1],l=0;l<c.length;++l){for(var m=0;2>m;++m)g=Math.min(g,c[l][m][0]),f=Math.min(f,c[l][m][1]),k=Math.max(k,c[l][m][0]),h=Math.max(h,c[l][m][1]);e.push([[c[l][0][0],c[l][0][1]],[c[l][1][0],c[l][1][1]]])}--g;--f;++k;++h;e.push([[g,f],[k,f]]);e.push([[k,f],[k,h]]);e.push([[k,h],[g,h]]);e.push([[g,h],[g,f]]);g=[];f=VisibilityPolygon.sortPoints(d,e);k=Array(e.length);for(l=0;l<k.length;++l)k[l]=-1;h=[];m=[d[0]+1,d[1]];for(l=0;l<
e.length;++l){var n=VisibilityPolygon.angle(e[l][0],d),p=VisibilityPolygon.angle(e[l][1],d),q=!1;-180<n&&0>=n&&180>=p&&0<=p&&180<p-n&&(q=!0);-180<p&&0>=p&&180>=n&&0<=n&&180<n-p&&(q=!0);q&&VisibilityPolygon.insert(l,h,d,e,m,k)}for(l=0;l<f.length;){var p=n=!1,q=l,m=e[f[l][0]][f[l][1]],r=h[0];do if(-1!=k[f[l][0]]?(f[l][0]==r&&(n=!0,m=e[f[l][0]][f[l][1]]),VisibilityPolygon.remove(k[f[l][0]],h,d,e,m,k)):(VisibilityPolygon.insert(f[l][0],h,d,e,m,k),h[0]!=r&&(p=!0)),++l,l==f.length)break;while(f[l][2]<f[q][2]+
VisibilityPolygon.epsilon());n?(g.push(m),n=VisibilityPolygon.intersectLines(e[h[0]][0],e[h[0]][1],d,m),VisibilityPolygon.equal(n,m)||g.push(n)):p&&(g.push(VisibilityPolygon.intersectLines(e[r][0],e[r][1],d,m)),g.push(VisibilityPolygon.intersectLines(e[h[0]][0],e[h[0]][1],d,m)))}return g};
VisibilityPolygon.computeViewport=function(d,c,e,g){for(var f=[],k=[[e[0],e[1]],[g[0],e[1]],[g[0],g[1]],[e[0],g[1]]],h=0;h<c.length;++h)if(!(c[h][0][0]<e[0]&&c[h][1][0]<e[0]||c[h][0][1]<e[1]&&c[h][1][1]<e[1]||c[h][0][0]>g[0]&&c[h][1][0]>g[0]||c[h][0][1]>g[1]&&c[h][1][1]>g[1])){for(var l=[],m=0;m<k.length;++m){var n=m+1;n==k.length&&(n=0);VisibilityPolygon.doLineSegmentsIntersect(c[h][0][0],c[h][0][1],c[h][1][0],c[h][1][1],k[m][0],k[m][1],k[n][0],k[n][1])&&(n=VisibilityPolygon.intersectLines(c[h][0],
c[h][1],k[m],k[n]),2==n.length&&(VisibilityPolygon.equal(n,c[h][0])||VisibilityPolygon.equal(n,c[h][1])||l.push(n)))}for(n=[c[h][0][0],c[h][0][1]];0<l.length;){for(var p=0,q=VisibilityPolygon.distance(n,l[0]),m=1;m<l.length;++m){var r=VisibilityPolygon.distance(n,l[m]);r<q&&(q=r,p=m)}f.push([[n[0],n[1]],[l[p][0],l[p][1]]]);n[0]=l[p][0];n[1]=l[p][1];l.splice(p,1)}f.push([n,[c[h][1][0],c[h][1][1]]])}c=[];for(h=0;h<f.length;++h)VisibilityPolygon.inViewport(f[h][0],e,g)&&VisibilityPolygon.inViewport(f[h][1],
e,g)&&c.push([[f[h][0][0],f[h][0][1]],[f[h][1][0],f[h][1][1]]]);f=10*VisibilityPolygon.epsilon();c.push([[e[0]-f,e[1]-f],[g[0]+f,e[1]-f]]);c.push([[g[0]+f,e[1]-f],[g[0]+f,g[1]+f]]);c.push([[g[0]+f,g[1]+f],[e[0]-f,g[1]+f]]);c.push([[e[0]-f,g[1]+f],[e[0]-f,e[1]-f]]);return VisibilityPolygon.compute(d,c)};
VisibilityPolygon.inViewport=function(d,c,e){return d[0]<c[0]-VisibilityPolygon.epsilon()||d[1]<c[1]-VisibilityPolygon.epsilon()||d[0]>e[0]+VisibilityPolygon.epsilon()||d[1]>e[1]+VisibilityPolygon.epsilon()?!1:!0};
VisibilityPolygon.inPolygon=function(d,c){for(var e=c[0][0],g=0;g<c.length;++g)e=Math.min(c[g][0],e),e=Math.min(c[g][1],e);for(var e=[e-1,e-1],f=0,g=0;g<c.length;++g){var k=g+1;k==c.length&&(k=0);if(VisibilityPolygon.doLineSegmentsIntersect(e[0],e[1],d[0],d[1],c[g][0],c[g][1],c[k][0],c[k][1])){var h=VisibilityPolygon.intersectLines(e,d,c[g],c[k]);if(VisibilityPolygon.equal(d,h))return!0;VisibilityPolygon.equal(h,c[g])?180>VisibilityPolygon.angle2(d,e,c[k])&&++f:VisibilityPolygon.equal(h,c[k])?180>
VisibilityPolygon.angle2(d,e,c[g])&&++f:++f}}return 0!=f%2};VisibilityPolygon.convertToSegments=function(d){for(var c=[],e=0;e<d.length;++e)for(var g=0;g<d[e].length;++g){var f=g+1;f==d[e].length&&(f=0);c.push([[d[e][g][0],d[e][g][1]],[d[e][f][0],d[e][f][1]]])}return c};
VisibilityPolygon.breakIntersections=function(d){for(var c=[],e=0;e<d.length;++e){for(var g=[],f=0;f<d.length;++f)if(e!=f&&VisibilityPolygon.doLineSegmentsIntersect(d[e][0][0],d[e][0][1],d[e][1][0],d[e][1][1],d[f][0][0],d[f][0][1],d[f][1][0],d[f][1][1])){var k=VisibilityPolygon.intersectLines(d[e][0],d[e][1],d[f][0],d[f][1]);2==k.length&&(VisibilityPolygon.equal(k,d[e][0])||VisibilityPolygon.equal(k,d[e][1])||g.push(k))}for(k=[d[e][0][0],d[e][0][1]];0<g.length;){for(var h=0,l=VisibilityPolygon.distance(k,
g[0]),f=1;f<g.length;++f){var m=VisibilityPolygon.distance(k,g[f]);m<l&&(l=m,h=f)}c.push([[k[0],k[1]],[g[h][0],g[h][1]]]);k[0]=g[h][0];k[1]=g[h][1];g.splice(h,1)}c.push([k,[d[e][1][0],d[e][1][1]]])}return c};VisibilityPolygon.epsilon=function(){return 1E-9};VisibilityPolygon.equal=function(d,c){return Math.abs(d[0]-c[0])<VisibilityPolygon.epsilon()&&Math.abs(d[1]-c[1])<VisibilityPolygon.epsilon()?!0:!1};
VisibilityPolygon.remove=function(d,c,e,g,f,k){k[c[d]]=-1;if(d==c.length-1)c.pop();else{c[d]=c.pop();k[c[d]]=d;var h=VisibilityPolygon.parent(d);if(0!=d&&VisibilityPolygon.lessThan(c[d],c[h],e,g,f))for(;0<d;){h=VisibilityPolygon.parent(d);if(!VisibilityPolygon.lessThan(c[d],c[h],e,g,f))break;k[c[h]]=d;k[c[d]]=h;var l=c[d];c[d]=c[h];c[h]=l;d=h}else for(;;){var h=VisibilityPolygon.child(d),m=h+1;if(h<c.length&&VisibilityPolygon.lessThan(c[h],c[d],e,g,f)&&(m==c.length||VisibilityPolygon.lessThan(c[h],
c[m],e,g,f)))k[c[h]]=d,k[c[d]]=h,l=c[h],c[h]=c[d],c[d]=l,d=h;else if(m<c.length&&VisibilityPolygon.lessThan(c[m],c[d],e,g,f))k[c[m]]=d,k[c[d]]=m,l=c[m],c[m]=c[d],c[d]=l,d=m;else break}}};VisibilityPolygon.insert=function(d,c,e,g,f,k){if(0!=VisibilityPolygon.intersectLines(g[d][0],g[d][1],e,f).length){var h=c.length;c.push(d);for(k[d]=h;0<h;){d=VisibilityPolygon.parent(h);if(!VisibilityPolygon.lessThan(c[h],c[d],e,g,f))break;k[c[d]]=h;k[c[h]]=d;var l=c[h];c[h]=c[d];c[d]=l;h=d}}};
VisibilityPolygon.lessThan=function(d,c,e,g,f){var k=VisibilityPolygon.intersectLines(g[d][0],g[d][1],e,f);f=VisibilityPolygon.intersectLines(g[c][0],g[c][1],e,f);if(!VisibilityPolygon.equal(k,f))return c=VisibilityPolygon.distance(k,e),e=VisibilityPolygon.distance(f,e),c<e;var h=0;VisibilityPolygon.equal(k,g[d][0])&&(h=1);var l=0;VisibilityPolygon.equal(f,g[c][0])&&(l=1);d=VisibilityPolygon.angle2(g[d][h],k,e);e=VisibilityPolygon.angle2(g[c][l],f,e);return 180>d?180<e?!0:e<d:d<e};
VisibilityPolygon.parent=function(d){return Math.floor((d-1)/2)};VisibilityPolygon.child=function(d){return 2*d+1};VisibilityPolygon.angle2=function(d,c,e){d=VisibilityPolygon.angle(d,c);c=VisibilityPolygon.angle(c,e);c=d-c;0>c&&(c+=360);360<c&&(c-=360);return c};VisibilityPolygon.sortPoints=function(d,c){for(var e=Array(2*c.length),g=0;g<c.length;++g)for(var f=0;2>f;++f){var k=VisibilityPolygon.angle(c[g][f],d);e[2*g+f]=[g,f,k]}e.sort(function(c,d){return c[2]-d[2]});return e};
VisibilityPolygon.angle=function(d,c){return 180*Math.atan2(c[1]-d[1],c[0]-d[0])/Math.PI};VisibilityPolygon.intersectLines=function(d,c,e,g){var f=g[0]-e[0],k=g[1]-e[1];g=c[0]-d[0];c=c[1]-d[1];var h=k*g-f*c;return 0!=h?(e=(f*(d[1]-e[1])-k*(d[0]-e[0]))/h,[d[0]-e*-g,d[1]-e*-c]):[]};VisibilityPolygon.distance=function(d,c){var e=d[0]-c[0],g=d[1]-c[1];return e*e+g*g};VisibilityPolygon.isOnSegment=function(d,c,e,g,f,k){return(d<=f||e<=f)&&(f<=d||f<=e)&&(c<=k||g<=k)&&(k<=c||k<=g)};
VisibilityPolygon.computeDirection=function(d,c,e,g,f,k){a=(f-d)*(g-c);b=(e-d)*(k-c);return a<b?-1:a>b?1:0};
VisibilityPolygon.doLineSegmentsIntersect=function(d,c,e,g,f,k,h,l){d1=VisibilityPolygon.computeDirection(f,k,h,l,d,c);d2=VisibilityPolygon.computeDirection(f,k,h,l,e,g);d3=VisibilityPolygon.computeDirection(d,c,e,g,f,k);d4=VisibilityPolygon.computeDirection(d,c,e,g,h,l);return(0<d1&&0>d2||0>d1&&0<d2)&&(0<d3&&0>d4||0>d3&&0<d4)||0==d1&&VisibilityPolygon.isOnSegment(f,k,h,l,d,c)||0==d2&&VisibilityPolygon.isOnSegment(f,k,h,l,e,g)||0==d3&&VisibilityPolygon.isOnSegment(d,c,e,g,f,k)||0==d4&&VisibilityPolygon.isOnSegment(d,
c,e,g,h,l)};