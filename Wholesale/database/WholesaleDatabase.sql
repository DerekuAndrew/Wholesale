USE master
GO

CREATE DATABASE wholesale_2026
GO

USE wholesale_2026
GO

CREATE TABLE [Clients] (
    ClientId INT IDENTITY(1,1) NOT NULL,
    ClientName VARCHAR(250) NOT NULL,
    ClientPhone VARCHAR(10) NULL,
    ClientEmail VARCHAR(100) NULL,
    ClientRfc VARCHAR(12) NOT NULL,
    ClientActive BIT NOT NULL,
    ClientCreatedAt DATETIME NOT NULL,
    ClientUpdatedAt DATETIME NOT NULL,

    CONSTRAINT PK_Client PRIMARY KEY (ClientId),
    CONSTRAINT UQ_ClientRfc UNIQUE (ClientRfc)
);
GO

CREATE TABLE [Locations] (
    LocationId INT IDENTITY(1,1) NOT NULL,
    ClientId INT NOT NULL,
    LocationName VARCHAR(250) NOT NULL,
    LocationAddress VARCHAR(250) NOT NULL,
    LocationCity VARCHAR(100) NOT NULL,
    LocationState VARCHAR(100) NOT NULL,
    LocationPostalCode VARCHAR(50) NOT NULL,
    LocationPhone VARCHAR(10) NULL,
    LocationEmail VARCHAR(100) NULL,
    LocationActive BIT NOT NULL,
    LocationCreatedAt DATETIME NOT NULL,
    LocationUpdatedAt DATETIME NOT NULL,

    CONSTRAINT PK_Location PRIMARY KEY (LocationId),
    CONSTRAINT FK_Location_Client FOREIGN KEY(ClientId) REFERENCES [Clients](ClientId)
);
GO

CREATE TABLE [Products] (
    ProductId INT IDENTITY(1,1) NOT NULL,
    ProductBarcode VARCHAR(100) NOT NULL,
    ProductName VARCHAR(250) NOT NULL,
    ProductDescription VARCHAR(250) NULL,
    ProductBrand VARCHAR(100) NULL,
    ProductPrice DECIMAL(16, 2) NOT NULL,
    ProductStock INT NOT NULL,
    ProductActive BIT NOT NULL,
    ProductCreatedAt DATETIME NOT NULL,
    ProductUpdatedAt DATETIME NOT NULL,

    CONSTRAINT PK_Product PRIMARY KEY (ProductId),
    CONSTRAINT UQ_ProductBarcode UNIQUE (ProductBarcode)
);
GO

CREATE TABLE [Sales] (
    SaleId INT IDENTITY(1,1) NOT NULL,
    SaleFolio VARCHAR(100) NOT NULL,
    LocationId INT NOT NULL,
    SaleDatetime DATETIME NULL,
    SaleTotal DECIMAL(16, 2) NULL,
    SaleStatus VARCHAR(100) NOT NULL,
    SaleCreatedAt DATETIME NOT NULL,
    SaleUpdatedAt DATETIME NOT NULL,

    CONSTRAINT PK_Sale PRIMARY KEY (SaleId),
    CONSTRAINT FK_Sale_Location FOREIGN KEY(LocationId) REFERENCES [Locations] (LocationId),
    CONSTRAINT UQ_SaleFolio UNIQUE (SaleFolio)
);
GO

CREATE TABLE [SaleDetails] (
    SaleDetailId INT IDENTITY(1,1) NOT NULL,
    SaleId INT NOT NULL,
    ProductId INT NOT NULL,
    SaleDetailQuantity INT NOT NULL,
    SaleDetailUnitPrice DECIMAL(16, 2) NOT NULL,
    SaleDetailSubtotal DECIMAL(16, 2) NOT NULL,

    CONSTRAINT PK_SaleDetail PRIMARY KEY (SaleDetailId),
    CONSTRAINT FK_SaleDetail_Sale FOREIGN KEY(SaleId) REFERENCES [Sales] (SaleId),
    CONSTRAINT FK_SaleDetail_Product FOREIGN KEY(ProductId) REFERENCES [Products] (ProductId)
);
GO
