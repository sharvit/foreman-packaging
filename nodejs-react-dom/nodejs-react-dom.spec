%global npm_name react-dom
%global enable_tests 0

Name: nodejs-%{npm_name}
Version: 16.2.0
Release: 1%{?dist}
Summary: React package for working with the DOM
License: MIT
Group: Development/Libraries
URL: https://reactjs.org/
Source0: https://registry.npmjs.org/react-dom/-/react-dom-16.2.0.tgz
Source1: https://registry.npmjs.org/loose-envify/-/loose-envify-1.3.1.tgz
Source2: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source3: https://registry.npmjs.org/prop-types/-/prop-types-15.6.0.tgz
Source4: https://registry.npmjs.org/fbjs/-/fbjs-0.8.16.tgz
Source5: https://registry.npmjs.org/js-tokens/-/js-tokens-3.0.2.tgz
Source6: https://registry.npmjs.org/isomorphic-fetch/-/isomorphic-fetch-2.2.1.tgz
Source7: https://registry.npmjs.org/promise/-/promise-7.3.1.tgz
Source8: https://registry.npmjs.org/setimmediate/-/setimmediate-1.0.5.tgz
Source9: https://registry.npmjs.org/core-js/-/core-js-1.2.7.tgz
Source10: https://registry.npmjs.org/whatwg-fetch/-/whatwg-fetch-2.0.3.tgz
Source11: https://registry.npmjs.org/ua-parser-js/-/ua-parser-js-0.7.17.tgz
Source12: https://registry.npmjs.org/node-fetch/-/node-fetch-1.7.3.tgz
Source13: https://registry.npmjs.org/asap/-/asap-2.0.6.tgz
Source14: https://registry.npmjs.org/encoding/-/encoding-0.1.12.tgz
Source15: https://registry.npmjs.org/is-stream/-/is-stream-1.1.0.tgz
Source16: https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.19.tgz
Source17: react-dom-16.2.0-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled-npm(react-dom) = 16.2.0
Provides: bundled-npm(loose-envify) = 1.3.1
Provides: bundled-npm(object-assign) = 4.1.1
Provides: bundled-npm(prop-types) = 15.6.0
Provides: bundled-npm(fbjs) = 0.8.16
Provides: bundled-npm(js-tokens) = 3.0.2
Provides: bundled-npm(isomorphic-fetch) = 2.2.1
Provides: bundled-npm(promise) = 7.3.1
Provides: bundled-npm(setimmediate) = 1.0.5
Provides: bundled-npm(core-js) = 1.2.7
Provides: bundled-npm(whatwg-fetch) = 2.0.3
Provides: bundled-npm(ua-parser-js) = 0.7.17
Provides: bundled-npm(node-fetch) = 1.7.3
Provides: bundled-npm(asap) = 2.0.6
Provides: bundled-npm(encoding) = 0.1.12
Provides: bundled-npm(is-stream) = 1.1.0
Provides: bundled-npm(iconv-lite) = 0.4.19
AutoReq: no
AutoProv: no

%define npm_cache_dir /tmp/npm_cache_%{name}-%{version}-%{release}
%description
%{summary}

%prep
mkdir -p %{npm_cache_dir}
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache %{npm_cache_dir} $tgz
done

%setup -T -q -a 17 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/react-dom
cp -pfr LICENSE README.md cjs index.js package.json server.browser.js server.js server.node.js test-utils.js umd unstable-native-dependencies.js node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf README.md LICENSE ../../

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%license LICENSE
%doc README.md

%changelog
* Thu Jan 04 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 16.2.0-1
- Update nodejs-react-dom to 16.2 (me@daniellobato.me)

* Tue Nov 07 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 16.0.0-1
- Update nodejs-react-dom to 16.0.0 (ewoud@kohlvanwijngaarden.nl)

* Thu Oct 05 2017 Eric D. Helms <ericdhelms@gmail.com> 15.6.2-1
- Update react-dom to 15.6.2 (me@daniellobato.me)

* Fri Oct 14 2016 Dominic Cleal <dominic@cleal.org> 15.3.2-1
- new package built with tito
