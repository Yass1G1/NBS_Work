// By Yassine Chouiti
// JS Script used as an Sheets Apps Script to fetch warranty status using Dell Website (reverse engineered) and a premade session cookie

function checkWarrantyDell(serial, cookieDell) {
    try {
      // Etape 1 : récuperer le cookie Dell (car sinon accès refusé aux autres sites) --> LANCER REQUETE WWW.DELL.COM ET LE RECUP DEPUIS LES DEVTOOLS
      //let tempCookie = "DellCEMSession=D6474EF80F535A8C3A32439A7EF5A285"; // à rajouter en paramètre lors de la mise en production, ne pas utiliser celui la
  
      // Etape 2 : récuperer le hash Dell de la réponse correspondant au numéro de série 
      //let tempHashSite = "https://www.dell.com/support/components/detectproduct/encvalue/25D8R93?appname=warranty";
      let hashSite = `https://www.dell.com/support/components/detectproduct/encvalue/${serial}?appname=warranty`;
  
  
      console.log("HashSite :")
      var hashRequestOptions = {
        "method": "get",
        "headers": {
          "User-Agent": "curl/8.5.0",
          "Accept": "*/*",
          "Cookie": cookieDell
        },
        "muteHttpExceptions": true // pour montrer les erreurs en entier
      };
      let hashRequest = UrlFetchApp.fetch(hashSite, hashRequestOptions);
      console.log("Hash request : " + hashRequest)
  
      let warrantyStatusSite = `https://www.dell.com/support/components/servicestore/fr-fr/ServiceStore/GetEligiblePONOffers?serviceTag=${hashRequest}`;
      let warrantyStatusReq = UrlFetchApp.fetch(warrantyStatusSite, hashRequestOptions);
  
  /* #### A REVOIR POUR SCRAPE LA DATE EXACT DE GARANTIE
      // 2ème requête qui passe le hash en paramètre du header pour vérifier la valeur de "onSupport" présent dans la réponse  
      console.log("ApiSite :")
      let apiSite = "https://www.dell.com/support/contractservices/fr-fr/entitlement/contractservicesapi/v1";
      var payload = {
          assetFormat: "servicetag",
          assetId: hashRequest,
          appName: "home"
      };
      var apiRequestOptions = {
        "method": "post",
        "headers": {
          "Content-Type": "application/json",
          "User-Agent": "curl/8.5.0", */
          //"Accept": "*/*", // à décommenter
  /*        "Cookie": cookieDell
        },
        "credentials": "include",
        "payload": JSON.stringify(payload),
        "muteHttpExceptions": true
      };
      let dellApiRequest = UrlFetchApp.fetch(apiSite, apiRequestOptions);
  */
  
      // Converti la réponse en JSON manipulable
      let warrantyStatus = JSON.parse(warrantyStatusReq); 
      //console.log(`warrantyStatus : ${warrantyStatus["IsInWarranty"]}`)
  
      return warrantyStatus["IsInWarranty"];
      //return dellApiRequest.toString();
    } catch (e) {
      return "Erreur : " + e.message;
    }
  }
  
  function checkWarrantyHP(serial) {
  
  }
  
  function checkWarrantyAsus(serial) {
  
  }
  
  function checkWarrantyLenovo(serial) {
  
  }
  